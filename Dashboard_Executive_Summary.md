# DASHBOARD EXECUTIVE SUMMARY: Q3 CAMPAIGN COMMAND CENTER

**Dashboard Name:** Seminole Hard Rock Hollywood - Q3 Direct Mail & Offer Tagging Command Center  
**Platform:** Looker Studio (Direct BigQuery Engine Connection)  
**Data Source:** `driiiportfolio.hard_rock_marketing.vw_cmp_q3_offer_tags`  

---

## Dashboard Architecture & Layout

The Looker Studio reporting suite is structured into three executive view modules:


```

+-----------------------------------------------------------------------------------+
| MODULE 1: EXECUTIVE KPI SCORECARDS                                                |
| [ Total Players: 50,000 ] [ Mailable: 47,500 (95%) ] [ Reinvestment: $4,825,000 ] |
+-----------------------------------------------------------------------------------+
| MODULE 2: OFFER TIER DISTRIBUTION            | MODULE 3: GEOGRAPHIC DENSITY      |
| - Guitar VIP Lux: 1,850 Players ($925k)       | - Top Zip: 33021 (Hollywood)      |
| - Oasis Suite: 6,200 Players ($1.24M)        | - Top Zip: 33314 (Davie/Hollyw.)  |
| - Boardwalk FreePlay: 14,100 Players ($1.41M)| - Suppressed Heatmap: Broward Cty |
| - General Gaming: 25,350 Players ($633k)     |                                   |
+-----------------------------------------------------------------------------------+

```

---

## Key Insights Rendered

1. **High-Value Concentration:** 1,850 players (3.7% of database) qualify for `OFFER_GUITAR_VIP_LUX` ($750+ ADT), driving 19.2% of total promotional reinvestment value ($925,000).
2. **Geographic Core:** 68% of mailable active players reside within a 25-mile radius of the Hollywood reservation (Broward and Palm Beach counties).
3. **Data Quality Health:** The 5.0% suppression rate is isolated primarily to legacy Classic cardholders, preserving 99.1% mailability among Platinum and Multi-Platinum VIP tiers.

---

## Operational User Instructions

* **Direct Mail Vendor Export:** Filter dashboard by `mail_deliverability_status = 'MAILABLE'` and click `Export to CSV` to generate the print vendor manifest.
* **CMP Offer Loading:** Filter by `q3_assigned_offer_tag` to export individual player list batches for CMP tag uploading.

```
