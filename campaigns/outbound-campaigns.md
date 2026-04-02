# Outbound Campaigns — Tongal

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
