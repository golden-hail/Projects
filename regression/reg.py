import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

telco = pd.read_excel('Telco_customer_churn.xlsx')

## Data notes
# all customers 'State' in Cali

olds_2_old_2_switch = telco.loc[(telco['Churn Value'] == 0) & (telco['Senior Citizen'] == 'Yes')]
olds_departed = telco.loc[(telco['Churn Value'] == 1) & (telco['Senior Citizen'] == 'Yes')]

print(f'{olds_2_old_2_switch.shape[0]} olds are too old to switch from this shitty service')
print(f'{olds_departed.shape[0]} olds are PEACING')

outski = telco.loc[telco['Churn Value'] == 1]

print(f'{outski.shape[0]} peeps are PEACING out of {telco.shape[0]}, which is a {outski.shape[0]/telco.shape[0] * 100} % churn, OUCH!')

outski[['CustomerID', 'Tenure Months', 'Phone Service',
'Multiple Lines', 'Internet Service', 'Online Security',
'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV',
'Streaming Movies', 'Contract', 'Paperless Billing', 'Payment Method',
'Monthly Charges', 'Total Charges', 'Churn Label', 'Churn Value',
'Churn Score', 'Churn Reason']]

old_left_2_comp = left_2_comp.loc[left_2_comp['Senior Citizen'] == 'Yes']

# Returns a filtered DataFrame
left_2_comp = outski[
    outski["Churn Reason"].str.contains("competitor", case=False, na=False)
]

# If you only want the 'Churn Reason' column values themselves
competitor_reasons = outski.loc[
    outski["Churn Reason"].str.contains("competitor", case=False, na=False),
    "Churn Reason",
]

telco.describe()

city_counts = telco.value_counts('City').reset_index

x = 
y = 

telco

plt.bar(telco['City'], )
plt.xlabel()
plt.ylabel()
plt.tight_layout()
plt.show()