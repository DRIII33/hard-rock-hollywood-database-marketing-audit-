# EXECUTIVE MEMORANDUM: Q3 DIRECT MAIL OFFER BUILDING & DATA HYGIENE AUDIT

**TO:** Director of Database Marketing, Seminole Hard Rock Hotel & Casino Hollywood  
**FROM:** Daniel Rodriguez III, Database Marketing Analyst  
**DATE:** August 30, 2026  
**SUBJECT:** Post-Audit Analysis & Direct Mail Yield Model for Q3 Guitar Hotel Campaign  

---

### 1. Executive Summary & Core Deliverables
An automated database marketing and player tagging pipeline was executed across 50,000 raw Casino Market Place (CMP) customer profiles to prepare the Q3 Guitar Hotel Direct Mail Campaign. By deploying automated address cleansing and National Change of Address (NCOA) standardization views in Google BigQuery, the database team successfully validated **48,761 mailable accounts** (97.52%) while automatically suppressing **1,239 unmailable accounts** (2.48%) containing corrupted zip codes or invalid street lines.

The total projected direct mail offer reinvestment budget across all mailable tiers is **$4,646,975.00**. Suppressing unmailable accounts prior to direct mail vendor list extraction prevents **$6,195.00** in immediate print, processing, and postage waste (evaluated at $5.00 per physical mailer).

---

### 2. Strategic Offer Matrix & Segment Yield Breakdown

The Q3 offer tagging engine evaluates guest Average Daily Theoretical Win (ADT) and verified Q2 visit frequency to assign tiered gaming credits and luxury stay offers:

| Offer Code | Segment Target | Minimum Qualification | Player Count | Offer Face Value | Total Spending Commitment | Mean Q2 ADT | Mean Coin-In |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OFFER_GUITAR_VIP_LUX** | Multi-Platinum / VIP | ADT $\ge \$750$ & Trips $\ge 3$ | 2,388 (4.78%) | $500.00 | $1,194,000.00 | $1,441.15 | $46,516.89 |
| **OFFER_OASIS_SUITE_STAY** | Platinum / High-Tier | ADT $\ge \$300$ & Trips $\ge 2$ | 6,603 (13.21%) | $200.00 | $1,320,600.00 | $594.34 | $15,835.63 |
| **OFFER_BOARDWALK_FP_100** | Gold / Core Players | ADT $\ge \$100$ & Trips $\ge 1$ | 15,175 (30.35%) | $100.00 | $1,517,500.00 | $230.18 | $5,572.62 |
| **OFFER_GENERAL_GAMING_25**| Classic / Low-Tier | ADT $< \$100$ or Trips $= 0$ | 24,595 (49.19%) | $25.00 | $614,875.00 | $62.50 | $1,474.99 |
| **NO_OFFER_BAD_ADDR** | Suppressed Records | Invalid Address / Zip `00000` | 1,239 (2.48%) | $0.00 | $0.00 | $248.68 | $6,761.87 |
| **TOTAL** | **Full Database Scope**| **All Active CMP Players** | **50,000** | **--** | **$4,646,975.00** | **$254.09** | **$6,897.29** |

---

### 3. Data Hygiene Audit & Statistical Validation

To ensure that address suppression rules do not create systemic bias against high-value VIP players, a **Chi-Square Test of Independence** was conducted comparing card tier status against mail deliverability status:

* **Null Hypothesis ($H_0$):** Address unmailability is independent of player card tier.
* **Alternative Hypothesis ($H_1$):** Address unmailability varies systematically by card tier.
* **Test Findings:** Chi-Square Statistic ($\chi^2$) = `1.3277`, Degrees of Freedom ($dof$) = `3`, $p$-value = `0.7226`.
* **Conclusion:** Because $p = 0.7226 > 0.05$, we fail to reject the null hypothesis. Invalid addresses occur randomly across Classic (627), Gold (360), Platinum (195), and Multi-Platinum (57) tiers. Automated suppression can be deployed in production without risking targeted VIP customer exclusion.

---

### 4. Operational Recommendations for Database Marketing

1. **Deploy Dynamic BigQuery Views to Production:** Shift direct mail extract logic from manual spreadsheet manipulation to `vw_q3_direct_mail_offers`, ensuring 100% repeatable vendor file extraction.
2. **Establish Host Remediation Workflows for Suppressed VIPs:** Export the 57 Multi-Platinum and 195 Platinum suppressed records (`NO_OFFER_BAD_ADDR`) to Executive Casino Hosts for phone/digital contact verification prior to campaign print deadlines.
3. **Automate Weekly CMP Ingestion Audits:** Implement daily data quality checks on incoming CMP tables to flag missing address lines before direct mail segmentation lists are frozen.
