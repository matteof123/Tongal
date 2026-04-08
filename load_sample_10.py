#!/usr/bin/env python3
"""
Load 10 sample Tongal leads into campaign 144.
2-step pattern: create with lowercase vars → update with UPPERCASE.
"""
import requests, json, time

BASE = "https://send.kinetyca.com"
KEY = "74|NaHF32H4MlKrXBjF6scxtwl1uybogJCZ1PNKBrjS7c9bacb7"
HEADERS = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json", "Accept": "application/json"}
CAMPAIGN_ID = 144
GOOGLE_SENDER_IDS = [32, 31, 28, 27, 26, 25, 24, 23, 22, 20]

def br(text):
    return text.replace("\n\n", "<br><br>").replace("\n", "<br>")

LEADS = [
    {
        "first_name": "Claire", "last_name": "Ivry Gonzales",
        "email": "claire.gonzales@alltrails.com", "company": "AllTrails",
        "title": "Head of Brand Partnerships",
        "sl_1": "AllTrails content clarity",
        "email_1": br("Hi Claire,\n\nAllTrails' platform effectively connects users with curated outdoor experiences and vibrant community content.\n\nTongal helps companies like BetterHelp cut CPA by 35% and achieve 50M+ impressions, and Samsung produce broadcast-quality video.\n\nI'd love to put together a Content Clarity Audit for AllTrails, showing new content opportunities. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "AllTrails video content",
        "email_2": br("Claire, high-quality video helps platforms like AllTrails deepen user engagement and visually share unique outdoor stories with new audiences.\n\nTongal helped BetterHelp cut CPA by 35% and gain 50M+ impressions. We offer 10-30 creative submissions per project, one team, and you own everything.\n\nWould it make sense to explore what a content package could look like for AllTrails?"),
        "ps_line": "If this isn't a fit, please let me know and I'll stop reaching out.",
    },
    {
        "first_name": "Kate", "last_name": "Gould",
        "email": "kate.g@matchmakingcompany.com", "company": "The Matchmaking Company",
        "title": "Director of Marketing and Technology",
        "sl_1": "Matchmaking Content Audit",
        "email_1": br("Hi Kate,\n\nThe Matchmaking Company's brand successfully conveys trust and personalized success stories through its client testimonials and discreet service approach.\n\nBrands like BetterHelp have cut CPA by 35% and achieved 50M+ impressions with creator-powered content.\n\nI'd love to put together a Content Clarity Audit for The Matchmaking Company, analyzing content strategy and creator-generated assets. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Matchmaking Video Ideas",
        "email_2": br("Kate, for a company like The Matchmaking Company, authentic video content builds immediate trust - vital for attracting new clients and sharing success stories.\n\nOur creator community helped brands like BetterHelp cut CPA by 35%. With Tongal, you work with one team and own all content outright.\n\nWould it make sense to explore what a content package could look like for The Matchmaking Company?"),
        "ps_line": "Happy to skip this if video content isn't on your radar right now.",
    },
    {
        "first_name": "Ryan", "last_name": "Tiffin",
        "email": "rtiffin@incrediblepizza.com", "company": "America's Incredible Pizza Company",
        "title": "Director of Marketing Operations",
        "sl_1": "Incredible Content Ideas",
        "email_1": br("Hi Ryan,\n\nYour marketing for America's Incredible Pizza Company effectively showcases the diverse attractions and family experiences across your channels.\n\nGlobal brands like LEGO and Nickelodeon use Tongal to produce broadcast-quality social content and scale creator-powered video.\n\nI'd love to put together a Content Clarity Audit for America's Incredible Pizza Company. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Ryan Video Content",
        "email_2": br("Ryan, video is essential for family entertainment centers like America's Incredible Pizza Company. It captures the excitement of rides, games, and events - communicating the fun that draws families.\n\nTongal's global creator community helps brands like LEGO produce broadcast-quality social content. Clients get 10-30 submissions per project and own everything outright.\n\nWould it make sense to explore what a content package could look like for America's Incredible Pizza Company?"),
        "ps_line": "No pressure at all - just let me know if this isn't relevant and I'll leave you alone.",
    },
    {
        "first_name": "Kelsey", "last_name": "Mckenna",
        "email": "kelsey@allthingsgo.world", "company": "All Things Go",
        "title": "Head of Brand Partnerships",
        "sl_1": "All Things Content",
        "email_1": br("Hi Kelsey,\n\nAll Things Go consistently produces engaging content that highlights artists and captures the festival's unique atmosphere.\n\nBrands like Nickelodeon, Disney, and LEGO have partnered with Tongal to produce broadcast-quality social content at scale.\n\nI'd love to put together a Content Clarity Audit for All Things Go, reviewing current trends and potential opportunities for brand integration. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "All Things Video",
        "email_2": br("Kelsey, for an organization like All Things Go, compelling video content is essential for attracting brand partners and engaging a global audience.\n\nTongal helped Nickelodeon create content at scale, delivering 10-30 creative submissions per project. With us, it's one team, and you own everything outright.\n\nWould it make sense to explore what a content package could look like for All Things Go?"),
        "ps_line": "If this isn't a fit, please let me know and I'll stop reaching out.",
    },
    {
        "first_name": "Matt", "last_name": "Stein",
        "email": "matt@philo.com", "company": "Philo",
        "title": "Head of Brand & Creative Strategy",
        "sl_1": "Philo Content Audit",
        "email_1": br("Hi Matt,\n\nPhilo's brand strategy for accessible entertainment and diverse programming clearly stands out in the streaming market.\n\nCompanies like Nickelodeon and Disney use our creator community for content at scale, achieving broad reach.\n\nI'd love to put together a Content Clarity Audit for Philo, reviewing your current content approach and identifying opportunities. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Philo Video Content",
        "email_2": br("Matt, in the competitive streaming landscape, compelling video content is essential to attract and retain subscribers and clearly communicate your unique channel lineup.\n\nOur creator community produced broadcast-quality content for Nickelodeon and Disney. You get 10-30 creative submissions, one team, and own everything outright.\n\nWould it make sense to explore what a content package could look like for Philo?"),
        "ps_line": "Happy to skip this if video content isn't on your radar right now.",
    },
    {
        "first_name": "Kara", "last_name": "Peneguy",
        "email": "kara@talentpop.co", "company": "TalentPop",
        "title": "Director of Marketing",
        "sl_1": "TalentPop Content Audit",
        "email_1": br("Hi Kara,\n\nYour content at TalentPop clearly articulates how remote teams help e-commerce brands scale efficiently.\n\nBrands like BetterHelp reduced CPA by 35% and gained over 50M impressions using creator-powered content.\n\nI'd love to put together a Content Clarity Audit for TalentPop, analyzing how your current video content performs and where opportunities exist. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "TalentPop video content",
        "email_2": br("Kara, video is a strong format for B2B services like TalentPop to demonstrate expertise and build trust with e-commerce clients. It communicates complex offerings and success stories well.\n\nSamsung creates broadcast-quality video and social content through our global creator community. You get 10-30 creative submissions per project, one team, and you own everything.\n\nWould it make sense to explore what a content package could look like for TalentPop?"),
        "ps_line": "No pressure at all - just let me know if this isn't relevant and I'll leave you alone.",
    },
    {
        "first_name": "Samantha", "last_name": "Set",
        "email": "samantha@feelgf.com", "company": "Feel Good Foods",
        "title": "VP of Marketing",
        "sl_1": "Feel Good Content",
        "email_1": br("Hi Samantha,\n\nYour team at Feel Good Foods consistently communicates the benefits of delicious, gluten-free options across your channels.\n\nWe help brands like BetterHelp cut CPA by 35% and LEGO create broadcast-quality social content.\n\nI'd love to put together a Content Clarity Audit for Feel Good Foods, examining content performance and potential. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Feel Good Video",
        "email_2": br("Samantha, engaging video content helps CPG brands like Feel Good Foods connect with consumers and showcase product benefits and lifestyle value.\n\nWe helped LEGO produce broadcast-quality social content with a global creator community. You get many creative options from one team, and you own everything outright.\n\nWould it make sense to explore what a content package could look like for Feel Good Foods?"),
        "ps_line": "If this isn't a fit, please let me know and I'll stop reaching out.",
    },
    {
        "first_name": "Christian", "last_name": "Riley",
        "email": "christian.riley@axiompest.com", "company": "Axiom Eco-Pest Control",
        "title": "Fractional CMO",
        "sl_1": "Axiom content audit",
        "email_1": br("Hi Christian,\n\nAxiom Eco-Pest Control's commitment to eco-friendly pest management sets a strong point of difference - there's a real story to tell here.\n\nBrands like BetterHelp cut CPA by 35% and gained 50M+ impressions with creator-powered content.\n\nI'd love to put together a Content Clarity Audit for Axiom, reviewing how your current content performs and where the gaps are. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Axiom video content",
        "email_2": br("Christian, for service companies like Axiom Eco-Pest Control, video turns a complex value proposition - eco-safe, effective, local - into something a homeowner immediately trusts.\n\nTongal's creator community helped BetterHelp cut CPA by 35% with 50M+ impressions. You get one team, you own everything outright.\n\nWould it make sense to explore what a content package could look like for Axiom?"),
        "ps_line": "Happy to skip this if video content isn't on your radar right now.",
    },
    {
        "first_name": "Hamid", "last_name": "Saify",
        "email": "hamid@luckybevco.com", "company": "Lucky Energy",
        "title": "Chief Marketing Officer",
        "sl_1": "Lucky Energy content",
        "email_1": br("Hi Hamid,\n\nLucky Energy's visual brand identity - the bold colors, positive energy angle - stands out in a crowded beverage market.\n\nLEGO produces broadcast-quality social content through Tongal's creator community, and Samsung scales video across markets with 10-30 creative submissions per project.\n\nI'd love to put together a Content Clarity Audit for Lucky Energy. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Lucky Energy video",
        "email_2": br("Hamid, for CPG beverage brands like Lucky Energy, video is the primary format to show the product in real moments and build a lifestyle around it.\n\nLEGO creates broadcast-quality social content through our global creator community. You get one team, and you own everything outright.\n\nWould it make sense to explore what a content package could look like for Lucky Energy?"),
        "ps_line": "No pressure at all - just let me know if this isn't relevant and I'll leave you alone.",
    },
    {
        "first_name": "Max", "last_name": "Kornblith",
        "email": "max.kornblith@citizen.health", "company": "Citizen Health",
        "title": "Head of Growth Marketing & Analytics",
        "sl_1": "Citizen Health content",
        "email_1": br("Hi Max,\n\nCitizen Health's mission to make healthcare accessible is clearly articulated across your platforms, especially in explaining complex health concepts simply.\n\nTongal's creator community helps brands like BetterHelp cut CPA by 35% and achieve 50M+ impressions.\n\nI'd love to put together a Content Clarity Audit for Citizen Health. No work from your team.\n\nWould you mind if I send the details?"),
        "sl_2": "Citizen Health video",
        "email_2": br("Max, for health tech companies like Citizen Health, video is key to explaining complex services and building trust with diverse audiences.\n\nOur global creator network delivers broadcast-quality content. BetterHelp used our model to cut CPA by 35%. With Tongal, it's one team, and you own everything outright.\n\nWould it make sense to explore what a content package could look like for Citizen Health?"),
        "ps_line": "If this isn't a fit, please let me know and I'll stop reaching out.",
    },
]

def step1_attach_senders():
    print("--- Step 1: Attaching Google senders ---")
    r = requests.post(f"{BASE}/api/campaigns/{CAMPAIGN_ID}/attach-sender-emails",
                      headers=HEADERS, json={"sender_email_ids": GOOGLE_SENDER_IDS})
    print(f"  Status: {r.status_code} | {r.text[:200]}")

def step2_create_leads_lowercase():
    print("\n--- Step 2: Creating leads with LOWERCASE vars ---")
    payload_leads = []
    for l in LEADS:
        payload_leads.append({
            "first_name": l["first_name"],
            "last_name": l["last_name"],
            "email": l["email"],
            "company": l["company"],
            "title": l["title"],
            "custom_variables": [
                {"name": "sl_1",    "value": l["sl_1"]},
                {"name": "email_1", "value": l["email_1"]},
                {"name": "sl_2",    "value": l["sl_2"]},
                {"name": "email_2", "value": l["email_2"]},
                {"name": "ps_line", "value": l["ps_line"]},
            ]
        })
    r = requests.post(f"{BASE}/api/leads/create-or-update/multiple",
                      headers=HEADERS, json={"existing_lead_behavior": "patch", "leads": payload_leads})
    print(f"  Status: {r.status_code}")
    data = r.json()
    print(f"  Response: {json.dumps(data)[:300]}")
    return data

def step3_update_leads_uppercase(lead_ids):
    print("\n--- Step 3: Updating leads with UPPERCASE vars ---")
    payload_leads = []
    for l, lid in zip(LEADS, lead_ids):
        payload_leads.append({
            "id": lid,
            "email": l["email"],
            "custom_variables": [
                {"name": "SL_1",    "value": l["sl_1"]},
                {"name": "EMAIL_1", "value": l["email_1"]},
                {"name": "SL_2",    "value": l["sl_2"]},
                {"name": "EMAIL_2", "value": l["email_2"]},
                {"name": "PS_LINE", "value": l["ps_line"]},
            ]
        })
    r = requests.post(f"{BASE}/api/leads/create-or-update/multiple",
                      headers=HEADERS, json={"existing_lead_behavior": "patch", "leads": payload_leads})
    print(f"  Status: {r.status_code} | {r.text[:300]}")

def step4_attach_to_campaign(lead_ids):
    print("\n--- Step 4: Attaching leads to campaign 144 ---")
    r = requests.post(f"{BASE}/api/campaigns/{CAMPAIGN_ID}/leads/attach-leads",
                      headers=HEADERS, json={"lead_ids": lead_ids, "allow_parallel_sending": True})
    print(f"  Status: {r.status_code} | {r.text[:300]}")

def extract_lead_ids(data):
    ids = []
    # Try common response shapes
    if isinstance(data, dict):
        for key in ["data", "leads", "results"]:
            if key in data:
                items = data[key]
                if isinstance(items, list):
                    for item in items:
                        if isinstance(item, dict) and "id" in item:
                            ids.append(item["id"])
                    if ids:
                        return ids
        # flat list at root
        if "id" in data:
            return [data["id"]]
    return ids

if __name__ == "__main__":
    step1_attach_senders()
    time.sleep(1)
    result = step2_create_leads_lowercase()
    lead_ids = extract_lead_ids(result)
    print(f"  Extracted lead IDs: {lead_ids}")

    if not lead_ids:
        print("ERROR: Could not extract lead IDs. Printing full response:")
        print(json.dumps(result, indent=2))
    else:
        time.sleep(1)
        step3_update_leads_uppercase(lead_ids)
        time.sleep(1)
        step4_attach_to_campaign(lead_ids)
        print(f"\n✓ Done. Campaign 144 now has {len(lead_ids)} leads (PAUSED — needs manual activation).")
        print(f"  Lead IDs: {lead_ids}")
