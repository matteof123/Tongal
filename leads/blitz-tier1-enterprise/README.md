# Tier 1 Enterprise — BlitzAPI Lead Sourcing

**Date:** 2026-04-10
**Source:** BlitzAPI (`/v2/search/companies` + `/v2/search/waterfall-icp-keyword` + `/v2/enrichment/email`)

## Target Criteria

| Filter | Value |
|---|---|
| Revenue | $200M+ (proxy: 1,000+ employees) |
| Headcount | 1,000+ |
| Industries | DTC/E-commerce, CPG/Food & Bev, Retail, Health & Wellness |

## ICP Titles (priority order)
1. CMO, Chief Marketing Officer, Chief Brand Officer, Chief Creative Officer, Chief Content Officer, Chief Growth Officer, Chief Communications Officer
2. VP Marketing, VP Creative, VP Brand, VP Content, VP Communications, VP Growth (and Vice President variants)
3. Head of Content, Head of Brand, Head of Marketing, Head of Creative, Creative Director, Director of Marketing, Director of Brand, Director of Content, Brand Director, Marketing Director

## Files
- `companies_cache.json` — 11,210 unique companies collected (raw, pre-ICP)
- `blitz_scraper.py` — scraper script used to generate this list
- `blitz_leads_tier1.json` — final enriched leads (contacts + emails)
- `blitz_leads_tier1.csv` — same data in CSV format
