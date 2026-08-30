# Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit

**Author:** Daniel Rodriguez III  
**Target Role:** Database Marketing Analyst (Requisition ID: R11492)  
**Primary Tech Stack:** Google BigQuery (`driiiportfolio`), Python (Google Colab, SciPy, Pandas), Looker Studio, Git/GitHub  

---

## 📌 Executive Overview
This project engineers an end-to-end automated direct mail offer building, address cleansing, and player tagging analytics pipeline for **Seminole Hard Rock Hotel & Casino Hollywood (The Guitar Hotel)**. Utilizing a synthetic dataset of 50,000 player records generated via Python, the solution processes raw Casino Market Place (CMP) extracts through Google BigQuery SQL views to standardize mailing addresses, apply National Change of Address (NCOA) suppression rules, assign dynamic Q3 gaming and hotel stay promotional offers based on Average Daily Theoretical Win (ADT), and generate executive campaign yield reports.

---

## 🎯 Alignment with Database Marketing Analyst Responsibilities

| Database Marketing Analyst Job Description Requirement | Project Deliverable & Implementation Mapping |
| :--- | :--- |
| **Database Management & SQL Querying** | Designed BigQuery DDL schemas (`01_raw_schema.sql`) with table clustering on card tier and city to optimize high-volume queries. |
| **Direct Mail List Preparation & Data Hygiene** | Built `02_address_cleansing_view.sql` to standardize street abbreviations, resolve zero-padded zip codes, and flag invalid addresses. |
| **CMP Offer Building & Player Tagging** | Engineered `03_offer_tagging_logic.sql` to dynamically tag player tiers with Q3 offers and suppress unmailable profiles. |
| **Campaign Yield & Statistical Analysis** | Authored `02_statistical_analysis.py` implementing a Chi-Square test ($\chi^2 = 1.3277, p = 0.7226$) verifying error randomness across tiers. |
| **Executive Dashboarding & Visualization** | Created `Dashboard_Executive_Summary.md` specifying a 3-page interactive Looker Studio dashboard detailing reinvestment metrics. |

---

## 🏗️ Technical Architecture & Pipeline Flow
