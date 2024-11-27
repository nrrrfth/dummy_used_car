#import library
import pandas as pd
from faker import Faker
import random

#membuat variable untuk generator-variable sbg fungsi Faker
fake = Faker()
#membuat instance Faker dengan lokal Indonesia
fake = Faker('id_ID')

#jumlah data yg dibutuhkan
n_bids = 300

# Contoh data bids
bids = {
    'bid_id': [fake.uuid4() for _ in range(n_bids)],
    'ad_id': [fake.uuid4() for _ in range(n_bids)],
    'buyer_id': [fake.uuid4() for _ in range(n_bids)],
    'bid_amount': [round(random.randint(90_000_000, 450_000_000), 2) for _ in range(n_bids)],
    'bid_date': [fake.date_time_this_year() for _ in range(n_bids)],
    'status_bid': [random.choice(['Pending', 'Accepted', 'Rejected']) for _ in range(n_bids)],
    'interaction_type': [random.choice(['View', 'Bid', 'Contract']) for _ in range(n_bids)],
    'bid_detail': []
}

# Mengisi bid_detail berdasarkan status bid
for i in range(n_bids):
    buyer = fake.name()
    bid_amount = bids['bid_amount'][i]
    status_bid = bids['status_bid'][i]

    if status_bid == 'Pending':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran sedang diproses."
    elif status_bid == 'Accepted':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran diterima."
    elif status_bid == 'Rejected':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran ditolak."

    bids['bid_detail'].append(detail)

# Membuat dataframe
df_bids = pd.DataFrame(bids)

# Menyimpan ke CSV
df_bids.to_csv('bids.csv', index=False)

print("Data telah diekspor ke bids.csv")