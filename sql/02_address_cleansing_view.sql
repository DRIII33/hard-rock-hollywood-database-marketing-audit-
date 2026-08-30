
-- =========================================================================================
-- Script Name: 02_address_cleansing_view.sql
-- Project: Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit
-- Author: Daniel Rodriguez III
-- Target Dataset: driiiportfolio.hard_rock_marketing
-- Description: Automated address cleansing, NCOA/CASS standardizations, and mail suppression flags.
-- Mapped Job Responsibility: Direct mail vendor list preparation & data hygiene governance.
-- =========================================================================================

CREATE OR REPLACE VIEW `driiiportfolio.hard_rock_marketing.vw_cleansed_player_mail` AS
WITH address_formatting AS (
    SELECT
        player_id,
        INITCAP(TRIM(first_name)) AS first_name,
        INITCAP(TRIM(last_name)) AS last_name,
        -- Standardize common street abbreviations and text casing
        INITCAP(
            REGEXP_REPLACE(
                REGEXP_REPLACE(TRIM(address_line1), r'(?i)st\.?', 'Street'),
                r'(?i)ave\.?', 'Avenue'
            )
        ) AS formatted_address_line1,
        INITCAP(TRIM(city)) AS city,
        UPPER(TRIM(state)) AS state,
        -- Pad 5-digit zip code string to resolve integer truncation (e.g., 00000 flags)
        LPAD(CAST(zip_code AS STRING), 5, '0') AS zip_code_5digit,
        cmp_card_tier,
        q2_adt_amount,
        q2_total_trips,
        q2_total_coin_in
    FROM `driiiportfolio.hard_rock_marketing.raw_cmp_player_extract`
)
SELECT
    player_id,
    first_name,
    last_name,
    formatted_address_line1,
    city,
    state,
    zip_code_5digit,
    cmp_card_tier,
    q2_adt_amount,
    q2_total_trips,
    q2_total_coin_in,
    -- Audit Flags
    CASE 
        WHEN zip_code_5digit = '00000' OR LENGTH(zip_code_5digit) < 5 THEN 1 
        ELSE 0 
    END AS is_invalid_zip_flag,
    CASE 
        WHEN formatted_address_line1 IS NULL OR TRIM(formatted_address_line1) = '' THEN 1 
        ELSE 0 
    END AS is_missing_address_flag,
    -- Deliverability Master Rule
    CASE 
        WHEN zip_code_5digit = '00000' OR LENGTH(zip_code_5digit) < 5 OR formatted_address_line1 IS NULL OR TRIM(formatted_address_line1) = '' 
        THEN 'SUPPRESS_UNMAILABLE'
        ELSE 'MAILABLE'
    END AS mail_deliverability_status
FROM address_formatting;
