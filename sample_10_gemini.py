#!/usr/bin/env python3
"""
Tongal — 10 sample leads copy via Gemini 2.5 Flash.
Prints results to stdout for human review before full run.
"""

import asyncio
import aiohttp
import json

GEMINI_API_KEY = "AIzaSyCgfjqfQEwmLWNumv-ArT9s727bikeHwR0"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

SYSTEM_PROMPT = """You are a cold email copywriter for Tongal, a creator-powered video production platform.

TONGAL PRODUCT: 160,000+ creators across 175 countries. Broadcast-quality video, animation, and social content. Clients get 10-30 creative submissions per project vs 2-3 from agencies. Faster, cheaper, clients own everything outright. Can produce locally anywhere in the world.

SENDER: Peter Kim, Account Manager at Tongal

CASE STUDIES (use ONLY these — never invent, match to industry):
- BetterHelp: cut CPA by 35%, 50M+ impressions (DTC, health/wellness, tech)
- LEGO: broadcast-quality social content via creator community (CPG, entertainment)
- Nickelodeon: creator-powered content at scale (entertainment, media)
- Disney: (entertainment, media, CPG)
- Samsung: broadcast-quality video and social content (tech, retail)
- Walden University: 6 graduate stories, 78 assets (education — use rarely)
- Bank of America: (financial — use rarely)

RULES (non-negotiable):
- 60-80 words per email body. Count carefully.
- NO em dashes (—). Use a dash (-) or three dots (...) instead.
- NO exclamation marks.
- NO spam words: free, boost, revolutionize, game-changer, unlock, leverage, synergy, transform, complimentary, innovative, cutting-edge, scalable, robust, seamless, solutions, comprehensive, elevate, drive/drives/driving, facilitate, align, crucial, ensuring/ensures, maximize, compelling, seamlessly, effectively
- NO negative framing. Never imply something is broken, missing, or wrong. Lead with positive outcomes.
- NO "impressive", "remarkable", or cheap compliments.
- NO signature text (no "Best,", no name, no title). Body ends at CTA.
- NO bracket placeholders like [first_name] — use the actual name.
- Subject lines: max 3 words. Company and person names Capitalized, other words lowercase. No punctuation.

EMAIL 1 STRUCTURE (lead magnet — Content Clarity Audit):
- Paragraph 1: Personalized hook — something specific and positive about this person or company's content/brand approach. State facts, not compliments.
- Paragraph 2: Social proof — brand names + a metric. Ends with a period.
- NEW PARAGRAPH: Audit offer — "I'd love to put together a Content Clarity Audit for [Company]..." + "No work from your team."
- CTA paragraph: "Would you mind if I send the details?"

EMAIL 2 STRUCTURE (service offer — new thread, NEVER references Email 1):
- Industry-specific angle on why video helps companies like theirs
- Case study reference + "one team, you own everything"
- CTA: "Would it make sense to explore what a content package could look like for [Company]?"

SUBJECT LINE RULES:
- SL_1 (Email 1): 3 words max, related to content/audit/brand
- SL_2 (Email 2): 3 words max, related to video/content
- Pattern to AVOID: "{Company} video production" — too generic
- Company names Capitalized, other words lowercase

Research the company and person using your knowledge before writing. Match case studies to their industry."""

LEADS = [
    {"first_name": "Claire", "last_name": "Ivry Gonzales", "company": "AllTrails", "website": "alltrails.com", "title": "Head of Brand Partnerships", "linkedin": "https://www.linkedin.com/in/claire-ivry-gonzales-50282930"},
    {"first_name": "Kate", "last_name": "Gould", "company": "The Matchmaking Company", "website": "matchmakingcompany.com", "title": "Director of Marketing and Technology", "linkedin": "https://www.linkedin.com/in/built-by-kate-gould"},
    {"first_name": "Ryan", "last_name": "Tiffin", "company": "America's Incredible Pizza Company", "website": "incrediblepizza.com", "title": "Director of Marketing Operations", "linkedin": "https://www.linkedin.com/in/ryantiffin"},
    {"first_name": "Kelsey", "last_name": "Mckenna", "company": "All Things Go", "website": "allthingsgofestival.com", "title": "Head of Brand Partnerships", "linkedin": "https://www.linkedin.com/in/kmckenna03"},
    {"first_name": "Matt", "last_name": "Stein", "company": "Philo", "website": "philo.com", "title": "Head of Brand & Creative Strategy", "linkedin": "https://www.linkedin.com/in/mattstein33"},
    {"first_name": "Kara", "last_name": "Peneguy", "company": "TalentPop", "website": "talentpop.co", "title": "Director of Marketing", "linkedin": "https://www.linkedin.com/in/karapeneguy"},
    {"first_name": "Samantha", "last_name": "Set", "company": "Feel Good Foods", "website": "feelgf.com", "title": "VP of Marketing", "linkedin": "https://www.linkedin.com/in/samantha-set"},
    {"first_name": "Christian", "last_name": "Riley", "company": "Axiom Eco-Pest Control", "website": "axiompest.com", "title": "Fractional CMO", "linkedin": "https://www.linkedin.com/in/rileychristian"},
    {"first_name": "Hamid", "last_name": "Saify", "company": "Lucky Energy", "website": "luckybevco.com", "title": "Chief Marketing Officer", "linkedin": "https://www.linkedin.com/in/hamidsaify"},
    {"first_name": "Max", "last_name": "Kornblith", "company": "Citizen Health", "website": "citizen.health", "title": "Head of Growth Marketing & Analytics", "linkedin": "https://www.linkedin.com/in/maxkornblith"},
]

PS_LINES = [
    "If this isn't a fit, please let me know and I'll stop reaching out.",
    "Happy to skip this if video content isn't on your radar right now.",
    "No pressure at all - just let me know if this isn't relevant and I'll leave you alone.",
]

async def write_copy_for_lead(session, lead, idx):
    user_prompt = f"""Write cold email copy for this lead. Research {lead['company']} ({lead['website']}) and {lead['first_name']}'s role as {lead['title']} before writing.

Lead:
- First name: {lead['first_name']}
- Company: {lead['company']}
- Title: {lead['title']}
- Website: {lead['website']}
- LinkedIn: {lead['linkedin']}

Return ONLY valid JSON with this exact structure:
{{
  "sl_1": "subject line email 1 (max 3 words)",
  "email_1": "full email 1 body (60-80 words, NO signature)",
  "sl_2": "subject line email 2 (max 3 words)",
  "email_2": "full email 2 body (60-80 words, NO signature)"
}}

Use \\n\\n between paragraphs. No markdown. No explanation outside the JSON."""

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": SYSTEM_PROMPT + "\n\n" + user_prompt}]}
        ],
        "generationConfig": {
            "responseMimeType": "application/json",
            "maxOutputTokens": 2048,
            "temperature": 0.7
        }
    }

    async with session.post(GEMINI_URL, json=payload) as resp:
        data = await resp.json()
        try:
            raw = data["candidates"][0]["content"]["parts"][0]["text"]
            # Fix literal newlines inside JSON strings
            import re
            raw_fixed = raw.strip().replace("\\'", "'")
            result = json.loads(raw_fixed)
            result["first_name"] = lead["first_name"]
            result["company"] = lead["company"]
            result["title"] = lead["title"]
            result["ps_line"] = PS_LINES[idx % len(PS_LINES)]
            return result
        except Exception as e:
            return {"error": str(e), "raw": str(data)[:300], "first_name": lead["first_name"], "company": lead["company"]}

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [write_copy_for_lead(session, lead, i) for i, lead in enumerate(LEADS)]
        results = await asyncio.gather(*tasks)

    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
