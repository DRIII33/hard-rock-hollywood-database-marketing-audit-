# Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit
**Entity:** Seminole Hard Rock Hotel & Casino Hollywood  
**Department:** Advertising & Promotions  
**Target Role:** Database Marketing Analyst (Requisition ID: R11492)  
**Author:** Daniel Rodriguez III  
**BigQuery Project ID:** `driiiportfolio`  

## Project Overview
This repository contains an end-to-end database marketing automation and data quality audit project engineered for Seminole Hard Rock Hotel & Casino Hollywood. The project addresses data quality issues in legacy player management databases (CMP/GHS/TIS), automates offer-tier tagging based on Average Daily Theoretical Win (ADT), normalizes player addresses for direct-mail vendor fulfillment, and generates an executive reporting suite in Looker Studio.

## Analytical Toolchain
* **Synthetic Data Engineering:** Python (`pandas`, `numpy`, `Faker`) executed via Google Colab.
* **Data Warehousing & SQL Analytics:** Google BigQuery (`driiiportfolio.hard_rock_marketing`).
* **Statistical Analysis:** Python (`scipy.stats`) for chi-square deliverability testing and ADT variance analysis.
* **Business Intelligence:** Looker Studio interactive executive dashboard.
* **Version Control:** GitHub repository.

## Key Deliverables
1. `Executive_Summary.md`: High-level strategic briefing for the Director of Advertising & Promotions.
2. `Dashboard_Executive_Summary.md`: Visual and operational guide for the Looker Studio reporting suite.
3. `Project_Disclaimer.md`: Professional portfolio disclosure and compliance statement.
4. `/sql/`: Production-ready BigQuery DDL and DML scripts.
5. `/notebooks/`: Executable Google Colab Python notebooks.

## Repository Setup & Execution Guide
1. Run `notebooks/01_synthetic_data_generation.ipynb` to generate `cmp_raw_player_extract.csv`.
2. Upload the CSV into Google BigQuery under dataset `driiiportfolio.hard_rock_marketing.raw_player_extract`.
3. Execute SQL scripts in `/sql/` sequentially (`01_raw_schema.sql` -> `02_address_cleansing_view.sql` -> `03_offer_tagging_logic.sql`).
4. Connect BigQuery view `vw_cmp_q3_offer_tags` to Looker Studio.
