# Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit

**Author:** Daniel Rodriguez III  
**Target Role:** Database Marketing Analyst (Requisition ID: R11492)  
**Primary Tech Stack:** Google BigQuery (`driiiportfolio`), Python (Google Colab, SciPy, Pandas), Looker Studio, Git/GitHub  

---

## Executive Overview

This project engineers an end-to-end automated direct mail offer building, address cleansing, and player tagging analytics pipeline for **Seminole Hard Rock Hotel & Casino Hollywood (The Guitar Hotel)**. Utilizing a synthetic dataset of 50,000 player records generated via Python, the solution processes raw Casino Market Place (CMP) extracts through Google BigQuery SQL views to standardize mailing addresses, apply National Change of Address (NCOA) suppression rules, assign dynamic Q3 gaming and hotel stay promotional offers based on Average Daily Theoretical Win (ADT), and generate executive campaign yield reports.

---

## Alignment with Database Marketing Analyst Responsibilities

| Database Marketing Analyst Job Description Requirement | Project Deliverable & Implementation Mapping |
| :--- | :--- |
| **Database Management & SQL Querying** | Designed BigQuery DDL schemas (`01_raw_schema.sql`) with table clustering on card tier and city to optimize high-volume queries. |
| **Direct Mail List Preparation & Data Hygiene** | Built `02_address_cleansing_view.sql` to standardize street abbreviations, resolve zero-padded zip codes, and flag invalid addresses. |
| **CMP Offer Building & Player Tagging** | Engineered `03_offer_tagging_logic.sql` to dynamically tag player tiers with Q3 offers and suppress unmailable profiles. |
| **Campaign Yield & Statistical Analysis** | Authored `02_statistical_analysis.py` implementing a Chi-Square test ($\chi^2 = 1.3277$, $p = 0.7226$) verifying error randomness across tiers. |
| **Executive Dashboarding & Visualization** | Created `Dashboard_Executive_Summary.md` specifying a 3-page interactive Looker Studio dashboard detailing reinvestment metrics. |

---

## Technical Architecture & Pipeline Flow


```

+----------------------------------------------------------------------------------------------------+
|                                    DATA PIPELINE FLOW CHART                                        |
+----------------------------------------------------------------------------------------------------+
| 1. SYNTHETIC ENGINE  : Python (01_synthetic_data.ipynb) --> Generates 50,000 CMP player profiles   |
| 2. DATA WAREHOUSE    : BigQuery (driiiportfolio.hard_rock_marketing.raw_cmp_player_extract)     |
| 3. DATA HYGIENE VIEW : BigQuery (vw_cleansed_player_mail) --> NCOA rules & zero-padding          |
| 4. OFFER RULE ENGINE : BigQuery (vw_q3_direct_mail_offers) --> ADT offer tiers & reinvestment     |
| 5. STATISTICAL YIELD : Python (02_statistical_analysis.py) --> Chi-square test & yield modeling |
| 6. BI DASHBOARD      : Looker Studio Executive Command Center --> Interactive KPI scorecards       |
+----------------------------------------------------------------------------------------------------+

```

---

## Key Campaign Performance Indicators (KPIs)

* **Total Database Audience:** 50,000 players
* **Mailable Audience (Passed NCOA/CASS Checks):** 48,761 players (97.52%)
* **Suppressed Audience (Unmailable / Invalid Address):** 1,239 players (2.48%)
* **Total Q3 Campaign Offer Reinvestment Spend:** $4,646,975.00
* **Automated Direct Mail Cost Avoidance:** $6,195.00 (saved at $5.00/mailer via suppression)
* **Chi-Square Independence Test Result:** $\chi^2 = 1.3277$, $dof = 3$, $p = 0.7226$ (Fail to reject $H_0$; address errors are unbiased across card tiers)

```
