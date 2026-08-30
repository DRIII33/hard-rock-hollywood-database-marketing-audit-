-- =========================================================================================
-- Script Name: 03_offer_tagging_logic.sql
-- Project: Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit
-- Author: Daniel Rodriguez III
-- Target Dataset: driiiportfolio.hard_rock_marketing
-- Description: Consolidated, production-validated reporting view for Looker Studio.
-- Source Layer: driiiportfolio.hard_rock_marketing.vw_cleansed_player_mail
-- Mapped Job Responsibility: CMP offer building, player segment tagging, & executive BI modeling.
-- =========================================================================================

CREATE OR REPLACE VIEW `driiiportfolio.hard_rock_marketing.vw_q3_direct_mail_offers` AS
SELECT
    player_id,
    first_name,
    last_name,
    address_line1,
    formatted_address_line1,
    city,
    state,
    zip_code_5digit,
    cmp_card_tier,
    q2_adt_amount,
    q2_total_trips,
    q2_total_coin_in,
    mail_deliverability_status,
    
    -- Dynamic Q3 Offer Tier Assignment Rule Engine
    CASE
        WHEN mail_deliverability_status = 'SUPPRESS_UNMAILABLE' THEN 'NO_OFFER_BAD_ADDR'
        WHEN q2_adt_amount >= 750 AND q2_total_trips >= 3 THEN 'OFFER_GUITAR_VIP_LUX'
        WHEN q2_adt_amount >= 300 AND q2_total_trips >= 2 THEN 'OFFER_OASIS_SUITE_STAY'
        WHEN q2_adt_amount >= 100 AND q2_total_trips >= 1 THEN 'OFFER_BOARDWALK_FP_100'
        ELSE 'OFFER_GENERAL_GAMING_25'
    END AS q3_assigned_offer_tag,
    
    -- Offer Description for Visual Tables & Reporting
    CASE
        WHEN mail_deliverability_status = 'SUPPRESS_UNMAILABLE' THEN 'Suppressed - Invalid Mailing Address'
        WHEN q2_adt_amount >= 750 AND q2_total_trips >= 3 THEN '$500 Free Play + 2-Night Guitar Hotel Luxury Suite'
        WHEN q2_adt_amount >= 300 AND q2_total_trips >= 2 THEN '$200 Free Play + 1-Night Oasis Tower Suite'
        WHEN q2_adt_amount >= 100 AND q2_total_trips >= 1 THEN '$100 Free Play Credit'
        ELSE '$25 General Gaming Free Play'
    END AS offer_description,

    -- Financial Reinvestment Value ($)
    CASE
        WHEN mail_deliverability_status = 'SUPPRESS_UNMAILABLE' THEN 0.00
        WHEN q2_adt_amount >= 750 AND q2_total_trips >= 3 THEN 500.00
        WHEN q2_adt_amount >= 300 AND q2_total_trips >= 2 THEN 200.00
        WHEN q2_adt_amount >= 100 AND q2_total_trips >= 1 THEN 100.00
        ELSE 25.00
    END AS offer_face_value_amount

FROM `driiiportfolio.hard_rock_marketing.vw_cleansed_player_mail`;
