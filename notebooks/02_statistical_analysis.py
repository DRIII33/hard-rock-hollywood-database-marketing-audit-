# =========================================================================================
# Script Name: 02_statistical_analysis.py
# Project: Guitar Hotel Q3 Direct Mail Offer Building & Player Tagging Automation Audit
# Author: Daniel Rodriguez III
# Target Role: Database Marketing Analyst (Req ID: R11492)
# Description: Statistical data quality validation (Chi-Square) & direct mail yield analysis.
# Mapped Job Responsibility: Campaign yield analysis, data audit automation, & executive metrics.
# =========================================================================================

import pandas as pd
import numpy as np
from scipy import stats

def run_campaign_statistical_audit(file_path="cmp_raw_player_extract.csv"):
    print("=" * 80)
    print("GUITAR HOTEL Q3 DIRECT MAIL CAMPAIGN STATISTICAL AUDIT & YIELD ANALYSIS")
    print("=" * 80)

    # 1. Load Data
    df = pd.read_csv(file_path)
    print(f"\n[INFO] Loaded dataset successfully. Total Records: {len(df):,}")

    # 2. Replicate Cleansing & Address Suppression Logic
    df['zip_str'] = df['zip_code'].astype(str).str.zfill(5)
    df['mail_deliverability_status'] = np.where(
        (df['zip_str'] == '00000') | (df['zip_str'].str.len() < 5), 
        'SUPPRESS_UNMAILABLE', 
        'MAILABLE'
    )

    # 3. Dynamic Offer Tagging Assignment Rule Engine
    def assign_q3_offer(row):
        if row['mail_deliverability_status'] == 'SUPPRESS_UNMAILABLE':
            return 'NO_OFFER_BAD_ADDR'
        elif row['q2_adt_amount'] >= 750 and row['q2_total_trips'] >= 3:
            return 'OFFER_GUITAR_VIP_LUX'
        elif row['q2_adt_amount'] >= 300 and row['q2_total_trips'] >= 2:
            return 'OFFER_OASIS_SUITE_STAY'
        elif row['q2_adt_amount'] >= 100 and row['q2_total_trips'] >= 1:
            return 'OFFER_BOARDWALK_FP_100'
        else:
            return 'OFFER_GENERAL_GAMING_25'

    df['q3_assigned_offer_tag'] = df.apply(assign_q3_offer, axis=1)

    # Offer Reinvestment Values
    offer_value_map = {
        'NO_OFFER_BAD_ADDR': 0.00,
        'OFFER_GUITAR_VIP_LUX': 500.00,
        'OFFER_OASIS_SUITE_STAY': 200.00,
        'OFFER_BOARDWALK_FP_100': 100.00,
        'OFFER_GENERAL_GAMING_25': 25.00
    }
    df['offer_face_value_amount'] = df['q3_assigned_offer_tag'].map(offer_value_map)

    # 4. CHI-SQUARE TEST OF INDEPENDENCE
    # Hypothesis Testing: Does unmailability depend on customer card tier?
    print("\n" + "-" * 50)
    print("STATISTICAL TEST 1: CHI-SQUARE INDEPENDENCE TEST")
    print("Null Hypothesis (H0): Address unmailability is independent of player card tier.")
    print("Alternative Hypothesis (H1): Address unmailability varies systematically by card tier.")
    print("-" * 50)

    contingency_table = pd.crosstab(df['cmp_card_tier'], df['mail_deliverability_status'])
    chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)

    print("\nContingency Table (Card Tier vs. Mail Status):\n", contingency_table)
    print(f"\nChi-Square Statistic: {chi2_stat:.4f}")
    print(f"Degrees of Freedom:  {dof}")
    print(f"p-value:             {p_val:.4f}")

    if p_val > 0.05:
        print("\n[VERDICT] Fail to Reject Null Hypothesis (p > 0.05).")
        print("RESULT: Invalid addresses are randomly distributed across loyalty tiers without systemic bias.")
    else:
        print("\n[VERDICT] Reject Null Hypothesis (p <= 0.05).")
        print("RESULT: Significant bias detected in missing/invalid addresses across card tiers.")

    # 5. FINANCIAL & REINVESTMENT YIELD MODELING
    print("\n" + "-" * 50)
    print("STATISTICAL TEST 2: Q3 CAMPAIGN REINVESTMENT SUMMARY")
    print("-" * 50)

    yield_summary = df.groupby('q3_assigned_offer_tag').agg(
        player_count=('player_id', 'count'),
        face_value=('offer_face_value_amount', 'first'),
        total_reinvestment=('offer_face_value_amount', 'sum'),
        mean_adt=('q2_adt_amount', 'mean'),
        median_adt=('q2_adt_amount', 'median'),
        mean_trips=('q2_total_trips', 'mean'),
        mean_coin_in=('q2_total_coin_in', 'mean')
    ).reset_index()

    total_mailable = (df['mail_deliverability_status'] == 'MAILABLE').sum()
    total_suppressed = (df['mail_deliverability_status'] == 'SUPPRESS_UNMAILABLE').sum()
    total_budget = df['offer_face_value_amount'].sum()
    cost_avoidance = total_suppressed * 5.00  # $5.00 estimated print + postage per mailer

    print(yield_summary.to_string(index=False))

    print("\n" + "=" * 50)
    print("EXECUTIVE KPI AUDIT SUMMARY")
    print("=" * 50)
    print(f"Total Player Audience Executed:      {len(df):,}")
    print(f"Total Mailable Players:              {total_mailable:,} ({total_mailable/len(df)*100:.2f}%)")
    print(f"Total Suppressed Players:            {total_suppressed:,} ({total_suppressed/len(df)*100:.2f}%)")
    print(f"Total Q3 Reinvestment Offer Budget:  ${total_budget:,.2f}")
    print(f"Direct Mail Waste Cost Avoidance:   ${cost_avoidance:,.2f} (Saved via automated suppression)")
    print("=" * 80)

if __name__ == "__main__":
    run_campaign_statistical_audit()
