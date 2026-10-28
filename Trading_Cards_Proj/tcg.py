# -*- coding: utf-8 -*-
"""
Business Context

You are a data analyst at Hobby Hub, a multi-region retailer that sells trading cards, 
booster packs, and accessories in stores and online. Leadership is planning 
2026 inventory and marketing budgets and needs answers to three questions:

1) Which franchises and product types drive the most revenue and margin, 
and where should inventory be expanded or cut?

2) How strong are seasonal and regional patterns, and when should promotions run?

3) Why are returns happening, and are they concentrated in particular channels, 
    products, or discount levels?
"""
import pandas as pd
import numpy as np

df = pd.read_csv('trading_card_sales_2024_2025.csv')

# Summarize num df - no negative values or nulls in numeric data
summ = df.describe()

#####################################################
# Data Cleaning
#####################################################

# Set expected data type category for each column in dict
expected_types = {
    'order_id': 'str', 'order_date': 'datetime', 'customer_id': 'str',
    'customer_segment': 'str', 'store_region': 'str', 'channel': 'str',
    'product_id': 'str', 'product_name': 'str', 'franchise': 'str',
    'product_type': 'str', 'quantity': 'int', 'unit_price': 'float',
    'unit_cost': 'float', 'discount_pct': 'int', 'net_revenue': 'float',
    'return_flag': 'int',
}

# Map data type category names to pandas dtype strings
type_mapping = {
    'str': ['object', 'string'],
    'int': ['int', 'Int'],
    'float': ['float', 'Float'],
    'datetime': ['datetime', 'date']
}

inconsistent_types = []

for col, exptype in expected_types.items():
    if col in df.columns:
        col_dtype = str(df[col].dtype)
        allowed_substrings = type_mapping[exptype]
        
        # Check if the col_dtype dtype matches set pandas category
        if not any(sub in col_dtype for sub in allowed_substrings):
            inconsistent_types.append((col, exptype, col_dtype))
            
        print(f"{col}: {col_dtype} (expected {exptype})")

print("\nMismatches:", inconsistent_types)

# Format date
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

df['order_date'].sort_values
df['order_date'].head(1) # 2024-01-01
df['order_date'].tail(1) # 2025-12-31

# Check for duplicate order_id (there is none)
df.duplicated().sum()

# Check for trailing spaces at the end of entries, trim them
df = df.replace(r'^\s*$', np.nan, regex=True).infer_objects(copy=False)

# Check for missing values (there are none)
for col in df.columns:
    a = df[col].isna().sum()
    print(col, a)

#####################################################
# Analysis
#####################################################

'''
Since we have 2 years worth of data, an appropriate measure of time would be monthly metrics
'''

# create month and year columns
df['month'] = df['order_date'].dt.month
df['year'] = df['order_date'].dt.year

## Gross margin is how much we made off of each item
# gross_margin = net_revenue - (unit_cost * quantity)
## total_cost is how much the company spent on the goods
df['total_cost'] = df['unit_cost'] * df['quantity']
df['gross_margin'] = df['net_revenue'] - df['total_cost']


''' monthly stats '''
# Group the data by months across the two years
mon_stats = df.groupby(['year', 'month'])[['net_revenue', 'total_cost', 'quantity', 'gross_margin']].sum()

# Percent margin
mon_stats['margin_pct'] = mon_stats['gross_margin'] / mon_stats['net_revenue']

# Average order value (AOV)
mon_stats['net_revenue'] / mon_stats['quantity'] 

# Return rate overall
mon_stats['return_rate'] = mon_stats['net_revenue'] / mon_stats['total_cost'] 
# SUM??

# return rate by franchise, product_type, channel
franchise = df.groupby(['franchise'])[['net_revenue', 'total_cost', 'quantity', 'gross_margin']].sum()
prod_type = df.groupby(['product_type'])[['net_revenue', 'total_cost', 'quantity', 'gross_margin']].sum()
channel = df.groupby(['channel'])[['net_revenue', 'total_cost', 'quantity', 'gross_margin']].sum()


'''
average order value, and return rate overall and by franchise, product type, and channel.
'''