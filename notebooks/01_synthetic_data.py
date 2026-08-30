!pip install faker

import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize seed for full reproducibility
fake = Faker()
Faker.seed(441)
np.random.seed(441)

NUM_PLAYERS = 50000

print("Generating 50,000 synthetic player profiles for Hard Rock Hollywood...")

player_ids = [f"CMP-{100000 + i}" for i in range(NUM_PLAYERS)]
first_names = [fake.first_name() for _ in range(NUM_PLAYERS)]
last_names = [fake.last_name() for _ in range(NUM_PLAYERS)]
addresses = [fake.street_address() for _ in range(NUM_PLAYERS)]
cities = np.random.choice(
    ['Hollywood', 'Fort Lauderdale', 'Miami', 'Boca Raton', 'West Palm Beach', 'Pembroke Pines'],
    NUM_PLAYERS,
    p=[0.30, 0.20, 0.20, 0.10, 0.10, 0.10]
)
states = ['FL'] * NUM_PLAYERS
zips = [fake.zipcode_in_state('FL') for _ in range(NUM_PLAYERS)]

# Introduce 5% controlled noise (missing street names, invalid zip codes) for data auditing
for i in random.sample(range(NUM_PLAYERS), int(NUM_PLAYERS * 0.05)):
    addresses[i] = addresses[i].lower().replace("street", "st.").replace("avenue", "ave")
    if i % 2 == 0:
        zips[i] = "00000"  # Unmailable flag condition

# Player Tier Distribution matching Casino Market Place (CMP) norms
card_tiers = np.random.choice(
    ['Classic', 'Gold', 'Platinum', 'Multi-Platinum'],
    NUM_PLAYERS,
    p=[0.50, 0.30, 0.15, 0.05]
)

# Theoretical Win (ADT) calculation based on player loyalty card status
adt_values = np.where(card_tiers == 'Multi-Platinum', np.random.uniform(800, 2500, NUM_PLAYERS),
             np.where(card_tiers == 'Platinum', np.random.uniform(300, 800, NUM_PLAYERS),
             np.where(card_tiers == 'Gold', np.random.uniform(100, 300, NUM_PLAYERS),
                      np.random.uniform(10, 100, NUM_PLAYERS))))

trips_q2 = np.random.poisson(lam=4, size=NUM_PLAYERS)
coin_in = adt_values * trips_q2 * np.random.uniform(5.5, 8.2, NUM_PLAYERS)

# Assemble Master DataFrame
df_raw = pd.DataFrame({
    'player_id': player_ids,
    'first_name': first_names,
    'last_name': last_names,
    'address_line1': addresses,
    'city': cities,
    'state': states,
    'zip_code': zips,
    'cmp_card_tier': card_tiers,
    'q2_adt_amount': np.round(adt_values, 2),
    'q2_total_trips': trips_q2,
    'q2_total_coin_in': np.round(coin_in, 2)
})

# Export raw dataset to CSV
df_raw.to_csv('cmp_raw_player_extract.csv', index=False)
print("SUCCESS: 'cmp_raw_player_extract.csv' generated with", len(df_raw), "records.")
