
-- =========================================================================================
-- Script Name: 01_raw_schema.sql
-- Project: Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit
-- Author: Daniel Rodriguez III
-- Target Dataset: driiiportfolio.hard_rock_marketing
-- Description: DDL to create raw staging table for Casino Market Place (CMP) player extracts.
-- Mapped Job Responsibility: Database management, relational data structuring, & staging logic.
-- =========================================================================================

CREATE OR REPLACE TABLE `driiiportfolio.hard_rock_marketing.raw_cmp_player_extract` (
    player_id STRING OPTIONS(description="Unique Casino Market Place (CMP) Player Account Identifier"),
    first_name STRING OPTIONS(description="Guest First Name"),
    last_name STRING OPTIONS(description="Guest Last Name"),
    address_line1 STRING OPTIONS(description="Primary Street Address Line"),
    city STRING OPTIONS(description="Municipality Name"),
    state STRING OPTIONS(description="Two-Letter State Code (FL)"),
    zip_code INT64 OPTIONS(description="Raw Zip Code extracted as Integer from CMP"),
    cmp_card_tier STRING OPTIONS(description="Casino Card Tier: Classic, Gold, Platinum, Multi-Platinum"),
    q2_adt_amount NUMERIC OPTIONS(description="Q2 Average Daily Theoretical Win ($)"),
    q2_total_trips INT64 OPTIONS(description="Q2 Verified Gaming Visit Count"),
    q2_total_coin_in NUMERIC OPTIONS(description="Q2 Total Slot Coin-In Volume ($)"),
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP() OPTIONS(description="Audit timestamp of data ingestion")
)
CLUSTER BY cmp_card_tier, city;
