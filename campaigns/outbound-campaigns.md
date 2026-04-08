# Outbound Campaigns — Tongal

---

## Sync Update — 2026-04-08

**AI hallucination crisis in Gemini-generated Email 1 copy. Wrong persona targeting (Sales, Client Success, PLG). Education vertical confirmed for removal. 3 new positive replies (NEOGOV, Evolve, Palm Beach Schools).**

### Metrics as of 2026-04-08

| ID | Campaign | Status | Leads | Sent | Replies (raw) | Replies (human) | Reply % (human) | Interested | Bounced | Bounce % | Completion % |
|----|----------|--------|-------|------|---------------|-----------------|-----------------|------------|---------|----------|-------------|
| 118 | Tongal Outlook to Google | Active | 1,587 | 2,723 | 152 | 27 | 1.0% | 4 | 20 | 0.7% | 89.0% |
| 86 | Tongal Google | Active | 3,318 | 4,469 | 222 | 32 | 0.7% | 1 | 62 | 1.4% | 69.0% |
| 87 | Tongal Outlook | Paused | 1,872 | 1,148 | 3 | ~2 | ~0.1% | 0 | 17 | 1.5% | 31.1% |
| 38 | Tongal Growth | Paused | 7,941 | 2,140 | 42 | ~17 | ~0.8% | 1 | 183 | 8.6% | 8.7% |

**Change vs 2026-04-02:** C118 sent +1,508 (+124%), completion 39%→89%. C86 sent +2,158 (+93%), completion 35%→69%. OOO inflation massive: 82% of C118 replies and 86% of C86 replies are automated.

---

### Tongal Google (86) — Copy Changes

_BEFORE = an ACTUAL email sent to a real lead, pulled from EmailBison conversation thread API. AFTER = suggested update based on reply intelligence from this sync._

---

#### Email 1 — BEFORE (actual email sent to Giselle Rahn at Evolve)

**Subject:** Evolve + video production

**Body:**
```
Hi Giselle,

Saw that you recently moved up to Senior Director, Marketing & Experience Design at Evolve.

Brands like Nike: We helped Nike scale authentic creator content through the Nike Creator Program, building deeper relationships with brand ambassadors., Disney: We helped Disney celebrate Alien's 40th anniversary by selecting 6 filmmakers from 550+ pitches to create fan-made shorts that debuted at major conventions. and BetterHelp: We helped BetterHelp drive platform sign-ups with a testimonial campaign that served 50M+ impressions and cut Cost Per Acquisition by 35%. use Tongal to produce broadcast quality video, animation, and social content through our global community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Evolve?

Peter Kim
Account Manager @ Tongal

P.S. In case this isn't a fit, please let me know and I'll stop reaching out.
```

**Their reply:** "Hi Peter, sure if you'd like to send a short summary over email that would be great. Thanks for reaching out." — Classification: POSITIVE (replied to Email 2 follow-up)

**Problems found in this actual email:**
- **AI HALLUCINATION (CRITICAL)**: Gemini dumped the ENTIRE case study description into the social proof line. Instead of "Brands like Nike, Disney and BetterHelp use Tongal...", the email says "Brands like Nike: We helped Nike scale authentic creator content through the Nike Creator Program, building deeper relationships with brand ambassadors., Disney: We helped Disney celebrate Alien's 40th anniversary by selecting 6 filmmakers from 550+ pitches to create fan-made shorts..." — This is unreadable and destroys credibility.
- **Industry mismatch**: Evolve is a vacation rental/hospitality company. Email 2 calls them a "Hospitality brand" but uses Nike as the case study — Nike is not hospitality.
- Despite these problems, the lead replied positively to Email 2. The Email 2 template (audit offer) is working even when Email 1 fails.

---

#### Email 1 — AFTER (suggested 2026-04-08)

**Subject:** Evolve's content

**Body:**
```
Hi Giselle,

Saw that you moved up to Senior Director at Evolve - congrats.

Brands like BetterHelp, Disney and Samsung use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Evolve?
```

**What changed and why:**
- **Case studies:** `Nike: We helped Nike scale...` (hallucinated paragraph) → `BetterHelp, Disney and Samsung` (clean brand names only) — Gemini AI must output ONLY brand names, never case study descriptions
- **Hook:** `recently moved up to Senior Director, Marketing & Experience Design` → `moved up to Senior Director` — simpler, less robotic
- **Word count:** ~180 words (broken) → 62 words (within 60-80 range)

**Root cause fix needed:** The Gemini prompt for Email 1 copy generation is pulling full case study descriptions from the context instead of just brand names. The prompt must explicitly instruct: "Output ONLY the brand name (e.g., 'Nike'), NEVER include the case study description."

---

#### Email 2 — NO CHANGE RECOMMENDED

_Email 2 (audit offer follow-up) is generating positive replies even when Email 1 has hallucination issues. Giselle at Evolve, Jackie at NEOGOV, and Gavin at Palm Beach all replied to Email 2. The template structure works. Keep as-is._

---

### Tongal Outlook to Google (118) — Copy Changes

---

#### Email 1 — BEFORE (actual email sent to Katie Fulton at Sierra Club)

**Subject:** Sierra Club + video production

**Body:**
```
Hi Katie Fulton,

Saw that you're leading a team of 10 digital strategists at Sierra Club who are driving innovative fundraising strategies.

Brands like Bank of America, Education.com and Xyzal use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Sierra Club?

Peter Kim
Account Manager @ Tongal

P.S. If this is not relevant, please let me know and I'll stop reaching out.
```

**Their reply:** "I am not interested. Please remove me from your email list." — Classification: NEGATIVE (not interested)

**Problems found in this actual email:**
- **Non-profit targeting**: Sierra Club is a non-profit environmental org — not in ICP (DTC, CPG, Retail, Health & Wellness)
- **Used full name "Katie Fulton" instead of first name "Katie"** — feels robotic
- **Personalization is vague**: "leading a team of 10 digital strategists driving innovative fundraising strategies" sounds like AI scraped LinkedIn and regurgitated it without filtering for relevance to video production
- Case studies (Bank of America, Education.com, Xyzal) don't match non-profit vertical

---

#### Email 1 — AFTER (suggested 2026-04-08)

_No AFTER needed for this specific lead — Sierra Club should not be in the campaign at all. The fix is TARGETING, not copy._

**Targeting fix required:**
- Remove non-profit organizations from lead lists
- Filter for ICP industries only: DTC, CPG, Retail, Health & Wellness, Entertainment, Toys (per April 8 call)
- Remove education vertical entirely (confirmed with Andy on April 8 call)

---

#### Email 1 — BEFORE (actual email sent to Eliot Cremin at Fivetran)

**Subject:** Fivetran + video production

**Body:**
```
Hi Eliot,

Saw that you recently moved up to Senior Product Growth Partner at Fivetran.

Brands like BetterHelp, Samsung and Nike use Tongal to create broadcast quality video, animation, and social content through our global community of 160,000 creators across 175 countries.

Agency-quality output, faster turnaround, lower cost and full ownership.

Worth exploring for Fivetran?

Peter Kim
Account Manager @ Tongal

PS: If this is not relevant, please let me know and I'll stop reaching out.
```

**Their reply:** "not relevant, I am not in that role since December" — Classification: NEGATIVE (wrong target)

**Problems found:**
- **Wrong persona**: Eliot Cremin is an Account Executive in Sales at Fivetran — not a creative/marketing decision-maker
- **Stale data**: "recently moved up to Senior Product Growth Partner" — she's been in a different role since December (4+ months)
- Similarly, Jess Tillis (Senior Director, PLG Revenue) at Fivetran also replied "not interested" — PLG Revenue is not the right persona

---

#### Email 1 — AFTER (suggested 2026-04-08)

_No copy AFTER needed — the fix is persona targeting:_

**Persona filter required:**
- Exclude: Account Executive, BDR, SDR, Sales, PLG, Growth (revenue-side), Client Success, Onboarding Specialist, Partner Marketing
- Include ONLY: CMO, VP Marketing, VP Creative, Head of Content, Creative Director, Head of Brand, Director of Marketing, Director of Content, Brand Manager (per ICP in CLAUDE.md)
- Validate job titles against ICP before loading leads

---

### Interested Replies — Email — 2026-04-08

| # | Person | Title | Company | Campaign | City/Region | Quote | New? |
|---|--------|-------|---------|----------|-------------|-------|------|
| 1 | Jackie Babe | Senior Creative Director | NEOGOV | C118 | - | "I'd love to see a quick summary and some examples via email" | NEW |
| 2 | Giselle Rahn | Sr Director, Marketing & Experience Design | Evolve | C86 | - | "Sure if you'd like to send a short summary over email that would be great" | NEW |
| 3 | Gavin Seidel | Social Studies Dept Head | Palm Beach Schools | C118 | FL | "Would be interested in reviewing a summary emailed so I can share with our Admin team" | NEW (but EDUCATION — flag for removal) |
| 4 | Scott Donaton | SVP, Global Head Brand & Community | Crunchyroll | C118 | - | "I know James well and am familiar with Tongal. Happy to facilitate a conversation" | From last sync |
| 5 | Jolanta Aerts | Creative Director | Vanta | C118 | - | "Do you happen to have a portfolio of your best case studies?" | From last sync |

**Patterns:**
- 3/5 interested replied to Email 2 (audit offer follow-up), not Email 1
- Positive replies cluster at Senior Director+ level at enterprise companies
- Palm Beach Schools is education — per April 8 call decision, education is being removed. This is the last education positive we'll see.
- Crunchyroll was warm (knew Tongal already) — copy didn't have to sell cold

### LinkedIn Campaigns — 2026-04-08

_HeyReach not yet active. LinkedIn contact list (~18,000) still being finalized. Per March 18 call: Tommy to review LinkedIn copy before launch._

> Added: 2026-04-02

---

## Sync Update — 2026-04-02

**First sync. Full pivot to Google-only sending confirmed. Outlook campaigns paused. Growth campaign paused due to broken variables and 8.6% bounce rate.**

### Metrics as of 2026-04-02

| ID | Campaign | Status | Leads | Sent | Replies | Reply % | Interested | Bounced | Bounce % | Completion % |
|----|----------|--------|-------|------|---------|---------|------------|---------|----------|-------------|
| 118 | Tongal Outlook to Google | Active | 1,587 | 1,215 | 57 | 4.7% | 2 | 9 | 0.7% | 39.0% |
| 86 | Tongal Google | Active | 3,318 | 2,311 | 105 | 4.5% | 0 | 47 | 2.0% | 35.4% |
| 87 | Tongal Outlook | Paused | 1,872 | 1,148 | 3 | 0.3% | 0 | 17 | 1.5% | 31.1% |
| 38 | Tongal Growth | Paused | 7,941 | 2,140 | 42 | 2.0% | 1 | 183 | 8.6% | 8.7% |

**OOO inflation warning:** The vast majority of "replies" across all campaigns are out-of-office auto-replies. Real human reply rate is estimated at ~1.5-2% for campaigns 86/118. Still strong, but metrics overstate engagement.

---

### Tongal Outlook to Google (118) — Copy

_This campaign uses short-form copy. 2 interested replies marked. Created 2026-03-28._

#### Email 1 — BEFORE (actual email sent to Jolanta Aerts at Vanta)

**Subject:** Vanta + video production

**Body:**
```
Hi Jolanta,

Noticed that you recently started as the Creative Director at Vanta.

Brands like BetterHelp, Samsung and Education.com use Tongal to create broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Vanta?

Peter Kim
Account Manager @ Tongal

PS: If this isn't a priority, please let me know and I'll stop reaching out.
```

**Their reply:** "Thanks for reaching out, I actually started 15 months ago. I've noticed that companies often reach out without sending any samples of their work. In the creative world, the output is the most important element of evaluation - do you happen to have a portfolio of your best case studies?" — Classification: POSITIVE

**Problems found in this actual email:**
- "Noticed that you recently started" — she started 15 months ago, not recently. Personalization data is stale.
- No portfolio link or specific work samples included
- Case studies (BetterHelp, Samsung, Education.com) don't match Vanta's industry (cybersecurity/compliance SaaS)
- Subject line "Vanta + video production" is generic

---

#### Email 1 — AFTER (suggested 2026-04-02)

**Subject:** Vanta's content

**Body:**
```
Hi Jolanta,

Saw Vanta's approach to building trust through transparency - the way you position compliance resonates.

Tongal helped BetterHelp cut CPA by 35% with a creator-driven testimonial campaign that served 50M+ impressions. Nickelodeon and Disney use us for broadcast and social content.

160,000 creators, 175 countries. You own everything.

Would it make sense to share a few relevant samples?

Peter Kim
Account Manager @ Tongal

PS: If this isn't a fit, let me know and I'll stop reaching out.
```

**What changed and why:**
- **Subject:** `Vanta + video production` → `Vanta's content` — removes generic "video production" pattern, feels more personal
- **Hook:** `Noticed that you recently started` → `Saw Vanta's approach to building trust` — removes stale job change data, leads with company observation
- **Case study:** Added BetterHelp CPA result (specific, measurable) alongside brand names
- **CTA:** `Worth exploring?` → `Would it make sense to share a few relevant samples?` — directly addresses what Jolanta asked for (portfolio)

---

#### Email 1 — BEFORE (actual email sent to Scott Donaton at Crunchyroll)

**Subject:** Crunchyroll + video production

**Body:**
```
Hi Scott,

Saw that you recently stepped into the SVP-Global Head of Brand & Community role at Crunchyroll.

Brands like Nickelodeon, Disney and LEGO use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Crunchyroll?

Peter Kim
Account Manager @ Tongal

P.S. If this isn't a fit, please let me know and I'll stop reaching out.
```

**Their reply:** "Hi, Peter, thanks for reaching out. I know James well and am familiar with Tongal. If you'd like to have James reach to me on this I'm happy to facilitate a conversation with our social content leads to see what can work." — Classification: POSITIVE

**Problems found in this actual email:**
- Copy worked well here — the prospect already knew Tongal/James, which drove the positive reply
- Subject line still follows generic "{Company} + video production" pattern
- Case studies (Nickelodeon, Disney, LEGO) are well-matched for entertainment/anime

#### Email 1 — NO CHANGE RECOMMENDED for entertainment/media segment

_This copy version works for entertainment targets. Nickelodeon/Disney/LEGO proof points are perfectly matched. The Crunchyroll reply proves this. Keep as-is for media/entertainment leads._

---

### Tongal Google (86) — Copy

_Largest active campaign. 3,318 leads, 4.5% reply rate. Same short-form copy template as campaign 118._

#### Email 1 — BEFORE (actual email sent to Maryann at Bleav)

**Subject:** Bleav + video production

**Body:**
```
Hi Maryann,

Saw that you recently stepped into the Director of Brand Partnerships role at Bleav.

Brands like Nickelodeon, Disney and LEGO use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Bleav?

Peter Kim
Account Manager @ Tongal

PS: In case this isn't a fit, please let me know and I'll stop reaching out.
```

**Their reply:** "Thanks for reaching out. This is outside my area of responsibility. I passed your email along to our team. If there is any interest they will reach out to you." — Classification: REFERRAL (warm)

**Problems found:**
- "Director of Brand Partnerships" may not be the right persona for video production decisions
- Copy is identical template to all other emails — no industry-specific angle

#### Email 1 — AFTER (suggested 2026-04-02)

_No structural change recommended for this campaign. The short-form template is working at 4.5% reply rate. Focus improvements on:_
1. **Subject line variety** — rotate away from "{Company} + video production" for every lead
2. **Case study matching** — media targets get Nickelodeon/Disney, tech gets BetterHelp/Samsung, education gets Walden University
3. **Persona validation** — filter out Brand Partnerships, BDR, and non-content roles before loading leads

---

### Tongal Growth (38) — Copy (PAUSED — Critical issues)

_Paused campaign with 8.6% bounce rate. Long-form copy with broken variable resolution._

#### Email 1 — BEFORE (actual email sent to Pete Schlosser at Evans Transportation)

**Subject:** Evans Transportation + video production

**Body:**
```
Hi Pete,

Saw that you recently took on the Chief Marketing Officer role at Evans Transportation.

Brands like Case Study 1, Case Study 2 and Case Study 3 use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Evans Transportation?

Peter Kim
Account Manager @ Tongal

P.S. If this isn't a priority, please let me know and I'll stop reaching out.
```

**Their reply:** "I appreciate you reaching out. We have a full marketing agency that handles all of our digital production as well as strategy. Feel free to reach out in the next 18 to 24 months as you never know how things change." — Classification: TIMING (has agency, come back later)

**Problems found in this actual email:**
- **CRITICAL: Broken variables** — "Case Study 1, Case Study 2 and Case Study 3" are literal placeholder text. The AI/Clay variables did not resolve.
- Transportation company receiving generic pitch — no industry-relevant proof points
- This is a SHOW-STOPPER bug. Any lead who received this email saw unresolved placeholders.

---

#### Email 1 (long form) — BEFORE (actual email sent to Ivy at Pendo.io)

**Subject:** video content for Pendoio Raleigh

**Body:**
```
Hi Ivy,

Saw that Pendo.io is expanding and actively hiring new talent. I took a look at how Pendoio handles content production and had a few thoughts.

Tongal is a creator-powered production platform that brands like BetterHelp, Samsung and Walden University use for everything from broadcast TV spots to social video and animation. We have 160,000+ creators across 175 countries, which means we can produce content wherever you need it, including locally in Raleigh.

What makes us different from a traditional agency: for every project, you get 10 to 30 creative submissions to choose from instead of the usual 2 to 3, delivery is faster, and you own everything outright.

We helped BetterHelp cut Cost Per Acquisition by 35% with a testimonial campaign that served over 50 million impressions. Same broadcast quality, completely different model.

If Pendoio is thinking about video production this quarter, even just social content or local stories I'd be happy to share how other IT brands use the platform.

Worth a conversation?

Peter Kim
Account Manager @ Tongal

P.S. In case this is not relevant, please let me know and I'll stop reaching out.
```

**Their reply:** "Hi Peter, you'll want to reach out to the marketing team. Not sales :)" — Classification: WRONG TARGET

**Problems found in this actual email:**
- **200+ words** — way over the 60-80 word limit
- **Wrong persona** — Ivy Linder is a BDR (Business Development Representative), not marketing
- **"Pendoio"** — company name misspelled throughout (it's Pendo.io or Pendo)
- **"IT brands"** — Pendo is a product analytics company, not an IT brand
- **Too much product explanation** — the long-form copy explains what Tongal is instead of showing social proof

#### Email 1 — AFTER (Growth campaign should NOT be relaunched)

_This campaign must remain paused. Issues:_
1. 8.6% bounce rate (unacceptable — damages sender reputation)
2. Broken case study variables ("Case Study 1, Case Study 2")
3. Long-form copy is 3x the recommended length
4. Persona targeting includes non-marketing roles
5. Company name errors (Pendoio → Pendo.io)

_All viable leads from this campaign should be migrated to campaigns 86 or 118 with the short-form copy template after re-verification._

---

### Tongal Outlook (87) — PAUSED

_0.3% reply rate. Correctly paused. Outlook sending infrastructure is not working for this client. All future sends should go through Google._

---

### Interested Replies — Email — 2026-04-02

| # | Person | Title | Company | Campaign | Reply Summary |
|---|--------|-------|---------|----------|---------------|
| 1 | Scott Donaton | SVP, Global Head of Brand & Community | Crunchyroll | 118 (Outlook to Google) | Knows James/Tongal, happy to facilitate conversation with social content leads |
| 2 | Jolanta Aerts | Creative Director | Vanta | 118 (Outlook to Google) | Interested, asked for portfolio and case study samples |
| 3 | Maryann (Bleav) | Director of Brand Partnerships | Bleav | 86 (Google) | Forwarded to team — warm referral |
| 4 | Melissa Drucker | Head of Global Brand Partnerships | MrBeast | 86 (Google) | Left company, forwarded to Beau Avril (beau@mrbeastyoutube.com) |
| 5 | Jonathan Yagel | Product Marketing | ClickUp | 86 (Google) | Left company, forwarded to Tariq Rauf (tariq@clickup.com) |
| 6 | Jeremy Sponder | VP, Global Catalog Development | Warner Music Group | 86 + 118 | Left company, forwarded to Brian Dodd (brian.dodd@rhino.com) |
| 7 | Debra Lashbrook | Senior Creative Director | Oakland University | 86 (Google) | Right person, but locked into 3-year vendor contract via RFP |
| 8 | Pete Schlosser | CMO | Evans Transportation | 38 (Growth) | Has agency, suggested reaching back in 18-24 months |

### Negative Replies — Targeting Issues — 2026-04-02

| # | Person | Title | Company | Campaign | Issue |
|---|--------|-------|---------|----------|-------|
| 1 | Ivy Linder | BDR | Pendo.io | 38 (Growth) | Wrong persona — BDR, not marketing |
| 2 | John Saboe | Social Studies Dept Head | Altoona Area School District | 38 (Growth) | Wrong persona — teacher, not marketing. Also wrong company type for video production |

> Added: 2026-04-02
