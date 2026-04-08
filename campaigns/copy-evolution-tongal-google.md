# Copy Evolution — Tongal Google
_Campaign ID: 86 | Client: Tongal_

---

## 2026-04-08

### Performance at this sync
| Metric | Value |
|--------|-------|
| Leads | 3,318 |
| Sent | 4,469 (+2,158 vs last sync) |
| Reply % (raw) | 3.5% (222 total replies) |
| Reply % (human) | 0.7% (32 non-automated) |
| Positive replies | 1 new (Evolve - Giselle Rahn, Sr Director Marketing) |
| Negative (target) | 2 (Fivetran x2 — wrong personas: Account Exec, PLG Revenue) |
| Negative (copy) | 1 (AI hallucination — full case study dumped into body) |
| Timing | 1 (Sprout Social — "in partner evaluation process") |
| Bounce % | 1.4% (62 bounced) |
| Completion | 69.0% |

### Reply Intelligence Summary
**Positive replies came from:** Sr Director, Marketing at Evolve (Hospitality). Replied to Email 2 (audit offer), NOT Email 1. Email 1 had massive AI hallucination but Email 2 still worked.
**Negative (target):** Fivetran — both Eliot Cremin (Account Executive/Sales) and Jess Tillis (Sr Director PLG Revenue) replied "not interested" / "not relevant". Neither is a creative/marketing decision-maker.
**Negative (copy):** AI hallucination in Evolve Email 1: Gemini dumped full case study descriptions into the social proof line. "Brands like Nike: We helped Nike scale authentic creator content through the Nike Creator Program..." — unreadable, destroys credibility.
**OOO inflation:** 190 of 222 replies (86%) are automated. Real human engagement is 32 replies from 4,469 sent (0.7%).

### Copy Changes Recommended

#### Email 1 — Critical Fix: AI Hallucination
**BEFORE (actual email sent to Giselle Rahn at Evolve):**
Subject: Evolve + video production
```
Hi Giselle,

Saw that you recently moved up to Senior Director, Marketing & Experience Design at Evolve.

Brands like Nike: We helped Nike scale authentic creator content through the Nike Creator Program, building deeper relationships with brand ambassadors., Disney: We helped Disney celebrate Alien's 40th anniversary by selecting 6 filmmakers from 550+ pitches to create fan-made shorts that debuted at major conventions. and BetterHelp: We helped BetterHelp drive platform sign-ups with a testimonial campaign that served 50M+ impressions and cut Cost Per Acquisition by 35%. use Tongal to produce broadcast quality video, animation, and social content through our global community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Evolve?
```

**AFTER (suggested 2026-04-08):**
Subject: Evolve's content
```
Hi Giselle,

Saw that you moved up to Senior Director at Evolve - congrats.

Brands like BetterHelp, Disney and Samsung use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for Evolve?
```

**Root cause:** Gemini 2.5 Flash prompt is pulling full case study descriptions from context instead of just brand names. Fix: add explicit instruction to Gemini prompt — "Output ONLY brand names (e.g., 'Nike'), NEVER include case study descriptions or results."

#### Email 2 — NO CHANGE
_Email 2 (audit offer) is generating all positive replies. Keep as-is._

### Targeting Changes Recommended

#### BEFORE — targeting as of 2026-04-02:
- Job titles: CMO, VP Marketing, VP Creative, Head of Content, Creative Director, plus broader titles
- Industries: DTC, CPG, Retail, Health & Wellness, Tech/SaaS
- Signals: New marketing leader, active hiring

#### AFTER — targeting suggested 2026-04-08:
- **Remove titles:** Account Executive, BDR, SDR, PLG Revenue, Client Success, Onboarding Specialist, Partner Marketing
- **Remove industries:** Education (confirmed April 8 call), Non-profits, Financial services
- **Add industries:** Toys, Healthcare (confirmed April 8 call)
- **Strictly enforce:** Marketing-related titles only, managers and above

**Evidence:**
- Fivetran: 2 negative replies from Sales/PLG roles — wrong persona
- Education: still generating replies (Aldine ISD, Palm Beach) but not revenue targets
- April 8 call: Andy confirmed focus on toys, entertainment, CPG, F&B, financial services, healthcare

---

## 2026-04-02

### Performance at this sync
| Metric | Value |
|--------|-------|
| Leads | 3,318 |
| Sent | 2,311 |
| Reply % | 4.5% (inflated by OOO) |
| Positive replies | ~5 (Bleav referral, MrBeast referral, ClickUp referral, Oakland warm, Warner referral) |
| Negative (target) | 0 confirmed on this campaign |
| Negative (copy) | 0 confirmed |
| Bounce % | 2.0% |

### Reply Intelligence Summary
**Positive replies came from:** SVP/Director-level at media and entertainment companies. Referrals from people who left companies suggest we're targeting the right companies but with stale contact data.
**Negative (target):** No confirmed wrong-target replies on this campaign (those were on Growth campaign 38).
**Negative (copy):** No confirmed copy complaints. The short-form template is not generating friction.
**OOO inflation:** Majority of 105 replies are auto-responses (maternity leave, PTO, OOO). Real human reply rate estimated ~2%.

### Copy Template (current — active)

**Subject:** {Company} + video production

**Body:**
```
Hi {First Name},

Saw that you recently stepped into the {Job Title} role at {Company}.

Brands like Nickelodeon, Disney and LEGO use Tongal to produce broadcast quality video, animation, and social content through our community of 160,000 creators across 175 countries.

Faster than an agency, a fraction of the cost, and you own everything.

Worth exploring for {Company}?

Peter Kim
Account Manager @ Tongal

PS: In case this isn't a fit, please let me know and I'll stop reaching out.
```

### Copy Changes Recommended

#### Subject Line
- **BEFORE:** `{Company} + video production` (every email, every lead)
- **AFTER:** Rotate between: `{Company}'s content`, `video for {Company}`, `{First Name} - quick question`
- **Why:** Every prospect sees the exact same pattern. Inbox fatigue. Variety improves open rates.

#### Case Study Matching
- **BEFORE:** Same 3 names regardless of industry (Nickelodeon, Disney, LEGO for everyone)
- **AFTER:** Match to vertical:
  - Media/Entertainment: Nickelodeon, Disney, LEGO (current — keep)
  - Tech/SaaS: BetterHelp, Samsung, Education.com
  - Education: Walden University, Education.com, Bank of America
  - Financial: Bank of America, Samsung, BetterHelp
  - Retail/F&B: (need new case studies — current portfolio weak here)
- **Why:** Bleav (media) got Nickelodeon/Disney — fine. But tech and edu targets need relevant proof.

#### Persona Filter
- **BEFORE:** Includes Brand Partnerships, BDR, and non-content roles
- **AFTER:** Strict filter to CMO, VP Marketing, Head of Content, Creative Director, Head of Brand, VP Creative
- **Why:** Bleav's Director of Brand Partnerships forwarded internally ("outside my area"). Correct titles convert directly.

### Targeting Changes Recommended
No major targeting changes for this campaign — it's performing well. Refinements:
- Add stricter job title filters (remove Brand Partnerships, Sales, BDR roles)
- Verify lead freshness — multiple "no longer with company" replies suggest stale data
- Continue Google-only sending

---

> Created: 2026-04-02
