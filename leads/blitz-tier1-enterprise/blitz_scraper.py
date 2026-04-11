#!/usr/bin/env python3
"""
BlitzAPI Tier 1 Enterprise Lead Scraper
Criteria: Revenue $200M+, 1,000+ employees
Industries: DTC/E-commerce, CPG/Food & Bev, Retail, Health & Wellness
Titles: CMO, VP Marketing, VP Creative, Head of Content, Creative Director, Head of Brand
"""

import time
import threading
import requests
import json
import csv
import os
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

BLITZ_KEY     = "blitz-019d2229-2198-79c0-9103-1c557e2cc83b"
FINDYMAIL_KEY = "eeVKsYJopsvqSyjwjKu0qCTiqqc5sRRhroEfrUQc01f1aec8"
LEADMAGIC_KEY = "4ca92dbb4c7963d17a8ef290c58093c7"
DEBOUNCE_KEY  = "662e8487018c1"

BASE = "https://api.blitz-api.ai"
HEADERS = {"x-api-key": BLITZ_KEY, "Content-Type": "application/json"}

FILTERED_CACHE   = "blitz_companies_filtered.json"
SKIP_FILE        = "blitz_companies_skipped.json"
ICP_CHECKPOINT   = "blitz_icp_checkpoint.json"   # incremental ICP saves
OUTPUT_JSON      = "blitz_leads_tier1.json"
OUTPUT_CSV       = "blitz_leads_tier1.csv"
CHECKPOINT_EVERY = 50   # save ICP results every N companies

# ── Industry groups mapped to BlitzAPI normalized values ──────────────────────
INDUSTRIES = [
    "Internet", "Consumer Goods", "Consumer Services",
    "Food and Beverages", "Food Production", "Wine and Spirits", "Dairy",
    "Retail", "Supermarkets", "Apparel and Fashion", "Luxury Goods and Jewelry",
    "Health, Wellness and Fitness", "Cosmetics", "Sporting Goods", "Alternative Medicine",
]

EMPLOYEE_RANGES = ["1001-5000", "5001-10000", "10001+"]

# Waterfall ICP cascade — priority order
CASCADE = [
    {
        "include_title": [
            "CMO", "Chief Marketing Officer", "Chief Brand Officer",
            "Chief Creative Officer", "Chief Content Officer",
            "Chief Growth Officer", "Chief Communications Officer",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator", "deputy"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
    {
        "include_title": [
            "VP Marketing", "VP of Marketing", "VP Creative", "VP of Creative",
            "VP Brand", "VP of Brand", "VP Content", "VP of Content",
            "VP Communications", "VP of Communications", "VP Growth", "VP of Growth",
            "Vice President Marketing", "Vice President of Marketing",
            "Vice President Creative", "Vice President of Creative",
            "Vice President Brand", "Vice President of Brand",
            "Vice President Content", "Vice President of Content",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
    {
        "include_title": [
            "Head of Content", "Head of Brand", "Head of Marketing",
            "Head of Creative", "Head of Communications", "Head of Growth",
            "Head of Digital Marketing", "Head of Social Media",
            "Creative Director", "Executive Creative Director", "Group Creative Director",
            "Director of Marketing", "Director of Brand", "Director of Content",
            "Director of Creative", "Director of Communications", "Director of Growth",
            "Director of Digital Marketing",
            "Brand Director", "Marketing Director", "Content Director", "Growth Director",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
]

# ── Rate limiter (5 req/s shared across all threads) ─────────────────────────
def make_rate_limiter(max_rps=5):
    timestamps = deque()
    lock = threading.Lock()

    def wait():
        with lock:
            while True:
                now = time.monotonic()
                while timestamps and timestamps[0] <= now - 1.0:
                    timestamps.popleft()
                if len(timestamps) < max_rps:
                    timestamps.append(time.monotonic())
                    return
                sleep_for = timestamps[0] + 1.0 - now + 0.01
                lock.release()
                try:
                    time.sleep(sleep_for)
                finally:
                    lock.acquire()
    return wait

rate_limit = make_rate_limiter(5)

def blitz(method, path, payload=None, timeout=30):
    url = f"{BASE}{path}"
    for attempt in range(3):
        try:
            rate_limit()
            if method == "GET":
                r = requests.get(url, headers=HEADERS, timeout=timeout)
            else:
                r = requests.post(url, headers=HEADERS, json=payload, timeout=timeout)

            if r.status_code == 429:
                print("  [429] Rate limited — waiting 60s...")
                time.sleep(60)
                continue
            if r.status_code in (402, 401):
                print(f"  [{r.status_code}] {r.text[:100]}")
                return None
            if r.status_code == 200:
                return r.json()
            time.sleep(2 ** attempt)
        except Exception as e:
            if attempt == 2:
                return None
            time.sleep(2)
    return None


# ── Step 1: Collect companies ─────────────────────────────────────────────────
def collect_companies(max_per_industry=999999):
    seen = set()
    all_companies = []

    for industry in INDUSTRIES:
        print(f"\n[Companies] Searching: {industry}")
        cursor = None
        page_count = 0
        industry_count = 0

        while True:
            payload = {
                "company": {
                    "industry": {"include": [industry]},
                    "employee_range": EMPLOYEE_RANGES,
                },
                "max_results": 25,
            }
            if cursor:
                payload["cursor"] = cursor

            result = blitz("POST", "/v2/search/companies", payload)
            if not result or not result.get("results"):
                break

            for c in result["results"]:
                url = c.get("linkedin_url", "")
                if url and url not in seen:
                    seen.add(url)
                    all_companies.append({
                        "company_name":     c.get("name", ""),
                        "company_linkedin": url,
                        "industry":         c.get("industry", industry),
                        "employee_count":   c.get("employee_count", ""),
                        "website":          c.get("website", ""),
                    })
                    industry_count += 1

            cursor = result.get("cursor")
            page_count += 1
            print(f"  Page {page_count}: {len(result['results'])} | total: {industry_count}")

            if not cursor or industry_count >= max_per_industry:
                break

    print(f"\n[Companies] Total unique companies: {len(all_companies)}")
    return all_companies


# ── Step 2: Waterfall ICP (concurrent, checkpointed) ─────────────────────────
def icp_worker(args):
    """Single ICP call — runs in thread pool."""
    i, total, company = args
    linkedin_url = company["company_linkedin"]
    result = blitz("POST", "/v2/search/waterfall-icp-keyword", {
        "company_linkedin_url": linkedin_url,
        "cascade": CASCADE,
        "max_results": 10,
    })

    contacts = []
    if result and result.get("results"):
        for r in result["results"]:
            p = r.get("person", {})
            if not p:
                continue
            contacts.append({
                "company_name":     company["company_name"],
                "company_linkedin": linkedin_url,
                "industry":         company["industry"],
                "employee_count":   company["employee_count"],
                "website":          company["website"],
                "full_name":        p.get("full_name", ""),
                "headline":         p.get("headline", ""),
                "linkedin_url":     p.get("linkedin_url", ""),
                "icp_tier":         r.get("icp", ""),
                "ranking":          r.get("ranking", ""),
                "email":            "",
                "email_source":     "",
                "email_status":     "",
                "email_found":      False,
            })
    return i, company["company_name"], contacts


def find_contacts(companies):
    # Load existing checkpoint
    all_contacts = []
    processed_urls = set()
    if os.path.exists(ICP_CHECKPOINT):
        with open(ICP_CHECKPOINT) as f:
            checkpoint = json.load(f)
        all_contacts = checkpoint.get("contacts", [])
        processed_urls = set(checkpoint.get("processed_urls", []))
        print(f"[ICP] Resuming from checkpoint: {len(processed_urls)} companies already done, {len(all_contacts)} contacts so far")

    # Filter out already-processed companies
    pending = [c for c in companies if c["company_linkedin"] not in processed_urls]
    total = len(companies)
    done = len(processed_urls)
    print(f"[ICP] {len(pending)} companies remaining to process ({done} already done)")

    save_lock = threading.Lock()

    def save_checkpoint():
        with save_lock:
            with open(ICP_CHECKPOINT, "w") as f:
                json.dump({
                    "contacts": all_contacts,
                    "processed_urls": list(processed_urls),
                }, f)

    # Run with 5 concurrent workers to saturate the 5 req/s rate limit
    batch = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        args_list = [(done + i + 1, total, c) for i, c in enumerate(pending)]
        futures = {executor.submit(icp_worker, args): args for args in args_list}

        completed_count = 0
        for future in as_completed(futures):
            i, company_name, contacts = future.result()
            company_linkedin = futures[future][2]["company_linkedin"]

            all_contacts.extend(contacts)
            processed_urls.add(company_linkedin)
            completed_count += 1

            status = f"{len(contacts)} contacts" if contacts else "none"
            print(f"  [{done + completed_count}/{total}] {company_name} → {status}")

            if completed_count % CHECKPOINT_EVERY == 0:
                save_checkpoint()
                print(f"  [Checkpoint] Saved {len(all_contacts)} contacts, {len(processed_urls)} companies processed")

    save_checkpoint()
    print(f"\n[ICP] Done. Total contacts: {len(all_contacts)}")
    return all_contacts


# ── Email helpers ─────────────────────────────────────────────────────────────
def _http_get(url, params=None, headers=None, timeout=15):
    try:
        r = requests.get(url, params=params, headers=headers, timeout=timeout)
        return r.json() if r.status_code == 200 else {}
    except Exception:
        return {}

def _http_post(url, payload=None, headers=None, timeout=15):
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=timeout)
        return r.json() if r.status_code in (200, 201) else {}
    except Exception:
        return {}

def validate_debounce(email):
    data = _http_get("https://api.debounce.io/v1/", params={"api": DEBOUNCE_KEY, "email": email})
    db = data.get("debounce", {})
    code = str(db.get("code", ""))
    result = db.get("result", "").lower()
    if code == "5" or "safe" in result:
        return "valid"
    if code == "6" or "invalid" in result:
        return "invalid"
    if code == "4" or "risky" in result or "accept_all" in result:
        return "risky"
    return "unknown"

def find_email_blitzapi(contact):
    li = contact.get("linkedin_url", "")
    if not li:
        return None
    result = blitz("POST", "/v2/enrichment/email", {"person_linkedin_url": li})
    if result and result.get("found"):
        email = result.get("email", "")
        return email if email and "@" in email else None
    return None

def find_email_findymail(contact):
    name = contact.get("full_name", "")
    website = contact.get("website", "")
    if not name or not website:
        return None
    domain = website.replace("https://", "").replace("http://", "").strip("/").split("/")[0]
    if not domain:
        return None
    data = _http_post(
        "https://app.findymail.com/api/search/name",
        payload={"name": name, "domain": domain},
        headers={"Authorization": f"Bearer {FINDYMAIL_KEY}", "Content-Type": "application/json"},
    )
    c = data.get("contact") or {}
    email = c.get("email") or data.get("email")
    return email if email and "@" in str(email) else None

def find_email_leadmagic(contact):
    name_parts = contact.get("full_name", "").split(" ", 1)
    first = name_parts[0] if name_parts else ""
    last  = name_parts[1] if len(name_parts) > 1 else ""
    website = contact.get("website", "")
    domain = website.replace("https://", "").replace("http://", "").strip("/").split("/")[0]
    payload = {"first_name": first, "last_name": last, "domain": domain}
    li = contact.get("linkedin_url", "")
    if li:
        payload["profile_url"] = li
    data = _http_post(
        "https://api.leadmagic.io/email-finder",
        payload=payload,
        headers={"X-API-Key": LEADMAGIC_KEY, "Content-Type": "application/json"},
    )
    email = data.get("email")
    return email if email and "@" in str(email) else None


# ── Step 3: Email enrichment waterfall (concurrent) ───────────────────────────
def email_waterfall_worker(args):
    """
    Waterfall: BlitzAPI → Debounce → FindyMail → LeadMagic → Debounce
    """
    i, total, contact = args
    email = source = status = ""

    # 1. BlitzAPI + Debounce
    blitz_email = find_email_blitzapi(contact)
    if blitz_email:
        s = validate_debounce(blitz_email)
        if s == "valid":
            email, source, status = blitz_email, "blitzapi", s

    # 2. FindyMail (pre-validated)
    if not email:
        fm_email = find_email_findymail(contact)
        if fm_email:
            email, source, status = fm_email, "findymail", "valid"

    # 3. LeadMagic + Debounce
    if not email:
        lm_email = find_email_leadmagic(contact)
        if lm_email:
            s = validate_debounce(lm_email)
            if s == "valid":
                email, source, status = lm_email, "leadmagic", s

    return i, contact, email, source, status


def enrich_emails(contacts):
    total = len(contacts)
    found = 0
    print_lock = threading.Lock()

    with ThreadPoolExecutor(max_workers=5) as executor:
        args_list = [(i + 1, total, c) for i, c in enumerate(contacts)]
        futures = {executor.submit(email_waterfall_worker, args): args for args in args_list}

        for future in as_completed(futures):
            i, contact, email, source, status = future.result()
            if email:
                contact["email"]        = email
                contact["email_source"] = source
                contact["email_status"] = status
                contact["email_found"]  = True
                found += 1
                with print_lock:
                    print(f"  [{i}/{total}] {contact['full_name']} → {email} ({source})")

    print(f"\n[Email] Enriched: {found}/{total} ({found/total*100:.1f}% hit rate)" if total else "")
    return contacts


# ── Step 4: Save output ───────────────────────────────────────────────────────
def save_output(contacts):
    with open(OUTPUT_JSON, "w") as f:
        json.dump(contacts, f, indent=2)

    if contacts:
        fields = list(contacts[0].keys())
        with open(OUTPUT_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(contacts)

    print(f"\n[Output] {len(contacts)} leads → {OUTPUT_JSON} + {OUTPUT_CSV}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    start = datetime.now()
    print("=" * 60)
    print("BlitzAPI Tier 1 Enterprise Lead Scraper")
    print(f"Started: {start.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    info = blitz("GET", "/v2/account/key-info")
    if not info or not info.get("valid"):
        print("[ERROR] API key invalid. Aborting.")
        return
    print(f"[Key] Valid | Credits: {info.get('remaining_credits','N/A')} | Rate: {info.get('max_requests_per_seconds',5)} req/s\n")

    # Step 1 — load filtered company list (pre-built by filter_companies.py)
    if os.path.exists(FILTERED_CACHE):
        with open(FILTERED_CACHE) as f:
            companies = json.load(f)
        print(f"[Companies] Loaded {len(companies)} companies from filtered cache")
    else:
        companies = collect_companies()
        with open(FILTERED_CACHE, "w") as f:
            json.dump(companies, f, indent=2)

    # Step 2
    print(f"\n[ICP] Starting Waterfall ICP on {len(companies)} companies (5 concurrent workers)...")
    contacts = find_contacts(companies)
    if not contacts:
        print("[ERROR] No contacts found.")
        return

    # Step 3
    print(f"\n[Email] Enriching {len(contacts)} contacts (5 concurrent workers)...")
    contacts = enrich_emails(contacts)

    # Step 4
    save_output(contacts)

    elapsed = int((datetime.now() - start).total_seconds())
    email_found = sum(1 for c in contacts if c["email_found"])
    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"  Companies processed: {len(companies)}")
    print(f"  Contacts found:      {len(contacts)}")
    print(f"  Emails enriched:     {email_found}")
    print(f"  Email hit rate:      {email_found/len(contacts)*100:.1f}%" if contacts else "")
    print(f"  Elapsed:             {elapsed}s")
    print("=" * 60)


if __name__ == "__main__":
    main()
