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
from datetime import datetime

BLITZ_KEY = "blitz-019d2229-2198-79c0-9103-1c557e2cc83b"
BASE = "https://api.blitz-api.ai"
HEADERS = {"x-api-key": BLITZ_KEY, "Content-Type": "application/json"}

OUTPUT_JSON = "blitz_leads_tier1.json"
OUTPUT_CSV  = "blitz_leads_tier1.csv"

# ── Industry groups mapped to BlitzAPI normalized values ──────────────────────
INDUSTRIES = [
    # DTC / E-commerce
    "Internet",
    "Consumer Goods",
    "Consumer Services",
    # CPG / Food & Bev
    "Food and Beverages",
    "Food Production",
    "Wine and Spirits",
    "Dairy",
    # Retail
    "Retail",
    "Supermarkets",
    "Apparel and Fashion",
    "Luxury Goods and Jewelry",
    # Health & Wellness
    "Health, Wellness and Fitness",
    "Cosmetics",
    "Sporting Goods",
    "Alternative Medicine",
]

# 1,000+ employees
EMPLOYEE_RANGES = ["1001-5000", "5001-10000", "10001+"]

# Waterfall ICP cascade — priority order
CASCADE = [
    {
        # CMO / Chief Marketing Officer and exact equivalents
        "include_title": [
            "CMO",
            "Chief Marketing Officer",
            "Chief Brand Officer",
            "Chief Creative Officer",
            "Chief Content Officer",
            "Chief Growth Officer",
            "Chief Communications Officer",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator", "deputy"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
    {
        # VP Marketing / VP Creative and synonyms
        "include_title": [
            "VP Marketing",
            "VP of Marketing",
            "VP Creative",
            "VP of Creative",
            "VP Brand",
            "VP of Brand",
            "VP Content",
            "VP of Content",
            "VP Communications",
            "VP of Communications",
            "VP Growth",
            "VP of Growth",
            "Vice President Marketing",
            "Vice President of Marketing",
            "Vice President Creative",
            "Vice President of Creative",
            "Vice President Brand",
            "Vice President of Brand",
            "Vice President Content",
            "Vice President of Content",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
    {
        # Head of Content / Head of Brand / Creative Director and synonyms
        "include_title": [
            "Head of Content",
            "Head of Brand",
            "Head of Marketing",
            "Head of Creative",
            "Head of Communications",
            "Head of Growth",
            "Head of Digital Marketing",
            "Head of Social Media",
            "Creative Director",
            "Executive Creative Director",
            "Group Creative Director",
            "Director of Marketing",
            "Director of Brand",
            "Director of Content",
            "Director of Creative",
            "Director of Communications",
            "Director of Growth",
            "Director of Digital Marketing",
            "Brand Director",
            "Marketing Director",
            "Content Director",
            "Growth Director",
        ],
        "exclude_title": ["assistant", "intern", "junior", "coordinator"],
        "location": ["WORLD"],
        "include_headline_search": False,
    },
]

# ── Rate limiter (5 req/s) ────────────────────────────────────────────────────
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
            if r.status_code == 402:
                print("  [402] Insufficient credits")
                return None
            if r.status_code == 401:
                print("  [401] Invalid API key")
                return None
            if r.status_code == 200:
                return r.json()
            print(f"  [{r.status_code}] {r.text[:200]}")
            time.sleep(2 ** attempt)
        except Exception as e:
            print(f"  [ERR] {e}")
            if attempt == 2:
                return None
            time.sleep(2)
    return None


# ── Step 1: Collect companies ─────────────────────────────────────────────────
def collect_companies(max_per_industry=200):
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
                        "company_name":      c.get("name", ""),
                        "company_linkedin":  url,
                        "industry":          c.get("industry", industry),
                        "employee_count":    c.get("employee_count", ""),
                        "website":           c.get("website", ""),
                    })
                    industry_count += 1

            cursor = result.get("cursor")
            page_count += 1
            print(f"  Page {page_count}: {len(result['results'])} companies | industry total: {industry_count}")

            if not cursor or industry_count >= max_per_industry:
                break

    print(f"\n[Companies] Total unique companies collected: {len(all_companies)}")
    return all_companies


# ── Step 2: Waterfall ICP per company ────────────────────────────────────────
def find_contacts(companies):
    contacts = []
    total = len(companies)

    for i, company in enumerate(companies, 1):
        linkedin_url = company["company_linkedin"]
        print(f"  [{i}/{total}] {company['company_name']}")

        result = blitz("POST", "/v2/search/waterfall-icp-keyword", {
            "company_linkedin_url": linkedin_url,
            "cascade": CASCADE,
            "max_results": 10,  # top 10 contacts per company
        })

        if not result or not result.get("results"):
            continue

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
                "email_found":      False,
            })

    print(f"\n[ICP] Contacts found: {len(contacts)}")
    return contacts


# ── Step 3: Email enrichment ──────────────────────────────────────────────────
def enrich_emails(contacts):
    total = len(contacts)
    found = 0

    for i, contact in enumerate(contacts, 1):
        li = contact.get("linkedin_url", "")
        if not li:
            continue

        print(f"  [{i}/{total}] {contact['full_name']} @ {contact['company_name']}")
        result = blitz("POST", "/v2/enrichment/email", {"person_linkedin_url": li})

        if result and result.get("found"):
            contact["email"] = result.get("email", "")
            contact["email_found"] = True
            found += 1
            print(f"    → {contact['email']}")
        else:
            print(f"    → not found")

    print(f"\n[Email] Enriched: {found}/{total}")
    return contacts


# ── Step 4: Save output ───────────────────────────────────────────────────────
def save_output(contacts):
    # Save JSON
    with open(OUTPUT_JSON, "w") as f:
        json.dump(contacts, f, indent=2)

    # Save CSV
    if contacts:
        fields = list(contacts[0].keys())
        with open(OUTPUT_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(contacts)

    print(f"\n[Output] Saved {len(contacts)} leads to:")
    print(f"  {OUTPUT_JSON}")
    print(f"  {OUTPUT_CSV}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    start = datetime.now()
    print("=" * 60)
    print("BlitzAPI Tier 1 Enterprise Lead Scraper")
    print(f"Started: {start.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Health check
    info = blitz("GET", "/v2/account/key-info")
    if not info or not info.get("valid"):
        print("[ERROR] API key invalid or unreachable. Aborting.")
        return
    print(f"[Key] Valid | Credits remaining: {info.get('remaining_credits', 'N/A')} | Rate limit: {info.get('max_requests_per_seconds', 5)} req/s\n")

    # Step 1 — use cached company list if available
    COMPANY_CACHE = "blitz_companies_cache.json"
    if os.path.exists(COMPANY_CACHE):
        with open(COMPANY_CACHE) as f:
            companies = json.load(f)
        print(f"[Companies] Loaded {len(companies)} companies from cache ({COMPANY_CACHE})")
    else:
        companies = collect_companies(max_per_industry=999999)
        if not companies:
            print("[ERROR] No companies found.")
            return
        with open(COMPANY_CACHE, "w") as f:
            json.dump(companies, f, indent=2)
        print(f"[Companies] Cached to {COMPANY_CACHE}")

    # Step 2
    print(f"\n[ICP] Running Waterfall ICP on {len(companies)} companies...")
    contacts = find_contacts(companies)
    if not contacts:
        print("[ERROR] No contacts found.")
        return

    # Step 3
    print(f"\n[Email] Enriching emails for {len(contacts)} contacts...")
    contacts = enrich_emails(contacts)

    # Step 4
    save_output(contacts)

    # Summary
    elapsed = (datetime.now() - start).seconds
    email_found = sum(1 for c in contacts if c["email_found"])
    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"  Companies scraped:   {len(companies)}")
    print(f"  Contacts found:      {len(contacts)}")
    print(f"  Emails enriched:     {email_found}")
    print(f"  Email hit rate:      {email_found/len(contacts)*100:.1f}%" if contacts else "  Email hit rate: N/A")
    print(f"  Elapsed:             {elapsed}s")
    print("=" * 60)


if __name__ == "__main__":
    main()
