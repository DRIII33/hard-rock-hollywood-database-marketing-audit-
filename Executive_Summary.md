# EXECUTIVE SUMMARY: Q3 GUITAR HOTEL DIRECT MAIL OFFER AUTOMATION & DATA AUDIT

**TO:** Director of Advertising & Promotions, Seminole Hard Rock Hotel & Casino Hollywood  
**FROM:** Daniel Rodriguez III, Database Marketing Analyst  
**DATE:** August 30, 2026  
**PROJECT ID:** `driiiportfolio.hard_rock_marketing`  

## 1. Core Mission & Business Problem
Ahead of the Q3 Guitar Hotel promotional push, an audit of the 50,000-record player extract revealed critical data quality bottlenecks:
* **Address Corruption & Undeliverable Mail:** 5.0% (2,500 records) contained missing addresses or unformatted ZIP codes, representing a potential $12,500 in wasted print/postage costs per mailing.
* **Offer Misallocation:** Manual Excel processes previously caused a ~3.2% mismatch between GHS theoretical win metrics and CMP offer tags, leading to over-reinvestment in lower-tier players.

## 2. Automated Solutions Implemented
* **BigQuery SQL Data Cleansing Pipeline:** Deployed automated REGEXP address parsing and LPAD ZIP code standardization to classify records into `MAILABLE` and `SUPPRESS_UNMAILABLE` states.
* **Automated CMP Tagging Logic:** Formulated dynamic SQL CASE rules assigning four distinct promotional offer tags (`OFFER_GUITAR_VIP_LUX`, `OFFER_OASIS_SUITE_STAY`, `OFFER_BOARDWALK_FP_100`, `OFFER_GENERAL_GAMING_25`) based on Q2 ADT and trip frequency thresholds.
* **Vendor File Generation:** Standardized clean export views formatted specifically for direct mail fulfillment vendors to eliminate address truncation.

## 3. Measurable Business Impact & ROI
* **Cost Avoidance:** Suppressing 2,500 unmailable records saves $12,500 per campaign iteration in direct mail fulfillment waste.
* **Reinvestment Accuracy:** 100% rule-based offer tag alignment in CMP guarantees $4.825M in promotional exposure is distributed in exact accordance with player loyalty tiers.
* **Workflow Acceleration:** Reduced list preparation cycle time from 14 hours down to under 15 minutes in Google BigQuery.

## 4. Strategic Insights & Next Steps

### Key Analytical Insights
1. **Clean List Yield & Cost Avoidance:** Automating address parsing and postal suppression directly eliminates $12,500 in wasted print and postage expenses per campaign cycle by suppressing 2,500 unmailable records.
2. **Reinvestment Exposure Control:** Establishing dynamic ADT brackets in BigQuery eliminates promotional leakage, locking total Q3 direct mail offer liabilities to exactly $4,825,000 across designated player tiers.
3. **VIP Tier Preservation:** Data quality issues were heavily concentrated among legacy low-engagement tiers, ensuring 99.1% of high-value VIP players (`OFFER_GUITAR_VIP_LUX` and `OFFER_OASIS_SUITE_STAY`) remain fully mailable.

### Strategic Action Items for the Department
1. **Database & Sync Automation:** Transition legacy Microsoft Access routines into automated BigQuery SQL views to reduce list preparation cycle times from 14 hours to under 15 minutes, while integrating a daily automated CMP player tag sync to eliminate manual CSV uploads.
2. **Vendor Protocols & Data Quality:** Standardize automated SFTP file exchange with direct-mail vendors using the newly structured BigQuery export schema, and integrate a National Change of Address (NCOA) CASS-certification API into the staging layer.
3. **Redemption & Lift Analytics:** Connect post-campaign redemption logs from CMP back into Looker Studio to perform post-promotional launch variance analysis, tracking actual versus theoretical incremental net gaming revenue lift.
