# -*- coding: utf-8 -*-
"""
To showcase both Linear/Logistic Regression and K-Nearest Neighbors (KNN) 
in a single data analyst portfolio project, the key is to construct a comparative 
modeling project. You will compare a parametric, interpretable model (Regression) 
against a non-parametric, instance-based model (KNN).

"Build a linear regression model to predict Customer Lifetime Value (CLTV) based on 
customer characteristics and service adoption. Compare the performance of models 
with different feature sets: (1) using only demographic and tenure data, 
(2) adding service subscriptions, and (3) including contract and payment 
information. Analyze which features are most predictive and explain the 
business implications of your findings."

https://www.kaggle.com/datasets/abdallahwagih/telco-customer-churn
"""

######################################################
# Import Data 
######################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Silence warnings
pd.set_option('future.no_silent_downcasting', True)

raw_data = pd.read_excel('telco_customer_churn.xlsx')

######################################################
# Phase 1: Data Cleaning & Feature Engineering
######################################################

# Drop irrelevent columns and duplicate entries
raw_data = raw_data.drop(columns = ['Count', 'Country', 'State', 'Lat Long', 'Latitude', 'Longitude', 'Gender', 'Senior Citizen', 'Partner', 'Churn Reason'])
raw_data.drop_duplicates(inplace=True)
desc = raw_data.describe()

# Check for data type uniformity for each variable in the dataset
for col in raw_data:
    unique_types = raw_data[col].map(type).unique()
    if len(unique_types) > 1:
        print(f"{col} has mixed data types")
    else:
        continue
    
# Convert raw whitespaces into NaNs
raw_data = raw_data.replace(r'^\s*$', np.nan, regex=True).infer_objects(copy=False)
# raw_data = raw_data.replace(r'^\s*$', 0, regex=True).infer_objects(copy=False)

# Check for NaNs. Churn reason has NaNs but we'll keep it for now
raw_data.isna().sum()

'''
a) Drop the column for Tenure Months == 0 as there is no data associated with these customers yet
'''
raw_data = raw_data[raw_data['Tenure Months'] != 0]

'''
b) Get a count of services that each customer
    # More difficult for customers with greater number of services to leave/switch
'''

services = ['Phone Service', 'Online Security', 'Online Backup', 'Device Protection', 
              'Tech Support', 'Streaming TV', 'Streaming Movies']

# Creates a True/False column for 'Yes' values and sums across rows (axis=1)
raw_data['service_count'] = (raw_data[services] == 'Yes').sum(axis=1)

'''
c) Prevent data leakage by... ML (why I chose these columns?) come back to this explanation
'''

from sklearn.model_selection import train_test_split

## categorical on city?? or drop it?
reg_data = raw_data['Tenure Months', 'Contract', 'Monthly Charges', 'Total Charges', 'CLTV', 'service_count']

# Define feature sets and target
target = 'Churn Value' 
categorical_vars = ["Contract"]
cols_2_standardize = ['Total Charges', 'Monthly Charges', 'CLTV', 'Tenure Months', 'addon_service_count']

# Select predictor features (X) and target (y)
X = raw_data[cols_2_standardize + categorical_vars].copy()
y = raw_data[target].copy()

# Train / Test Split (PREVENTS LEAKAGE)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# check this out somewhere
raw_data.corr() 

'''
d) OneHotEncoder categorical variable 'Contract' (feature encoding))
'''

from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Instantiate class; specify <drop = 'first'> to avoid the dummy variable trap!
one_hot_encoder = OneHotEncoder(sparse_output = False, drop = 'first') 

# **FIT & TRANSFORM on Training set ONLY**

# The encoder learns category names strictly from X_train
X_train_encoded_array = one_hot_encoder.fit_transform(X_train[categorical_vars])

# Assign the new binary nparrays their original column names (excluding the 'first' dropped column)
encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

# Convert numpy array back into a pandas DataFrame using X_train's index
X_train_contract = pd.DataFrame(
    X_train_encoded_array, 
    columns=encoder_feature_names, 
    index=X_train.index
)

# TRANSFORM ONLY on Test set
# Uses category rules learned from X_train (No .fit() here!)
X_test_encoded_array = one_hot_encoder.transform(X_test[categorical_vars])

X_test_contract = pd.DataFrame(
    X_test_encoded_array, 
    columns=encoder_feature_names, 
    index=X_test.index
)

## Note, if Contract_One year and Contract_Two year are 0 for a client, they have a month-to-month plan

'''
## Standardize the data of interest with Feature Scaling 
'''

# Instantiate Scaler
scale_standard = StandardScaler()

# apply the fit method to apply the rules of scaling 
# and then transform method to apply the scaling method to our data

# FIT & TRANSFORM on Training set ONLY
    # Scaler calculates mean & std dev from X_train and rescales the numbers

scaled_train_array = scale_standard.fit_transform(X_train[cols_2_standardize])

# Create a clean DataFrame for scaled training numerics
X_train_num = pd.DataFrame(
    scaled_train_array,
    columns=[f"{col} Standardized" for col in cols_2_standardize],
    index=X_train.index
)

# TRANSFORM ONLY on Test set
# Scales X_test using the mean & std dev saved from X_train (No .fit() here!)
scaled_test_array = scale_standard.transform(X_test[cols_2_standardize])

# Create a clean DataFrame for scaled test numerics
X_test_num = pd.DataFrame(
    scaled_test_array,
    columns=[f"{col} Standardized" for col in cols_2_standardize],
    index=X_test.index
)

'''
## Combine target and input data into a single modeling dataset 
'''
# Merge scaled numerics and encoded categoricals for Training set
X_train_final = pd.concat([X_train_num, X_train_contract], axis=1)

# Merge scaled numerics and encoded categoricals for Test set
X_test_final = pd.concat([X_test_num, X_test_contract], axis=1)

print("Preprocessing complete!")
print("\nShape of X_train_final:", X_train_final.shape)
print("Features in X_train_final:\n", X_train_final.columns.tolist())

######################################################
# Phase 2: Churn Risk Classification (Logistic Regression)
######################################################

'''
* Identify high-risk churn profiles with logistic regression
'''

# Tenure Months: Ranges from 0 to 72
# Monthly Charges: Ranges from $18 to $118
# Service_Count: Ranges from 0 to 6 
# Contract
# churn score is y??

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Instantiate our classification model object
clf = LogisticRegression

# ???Train our model... why are we doing this again??
clf.fit(X_train, y_train)

## Do we need feature selection?? 

######################################################
# Phase 4: Financial & Lifetime Value Drivers (Linear Regression)
######################################################




## Notes:
    # Churn Score is a column we'd get from a data science team with ML 


'''
Geographic variables (City/Zip) were excluded from predictive modeling 
to avoid high feature dimensionality, but preliminary spatial EDA 
identified high churn concentrations in [City X] that warrant localized 
field investigations... 

(probably service competition in those areas and zipcodes)

'''

# churned members per city
churned = telco.loc[(telco['Churn Value'] == 1)]
churn_city = churned.groupby('City').size().reset_index(name = 'Churn Count')

# non-churned members per city
cust = telco.loc[(telco['Churn Value'] == 0)]
cust_city = cust.groupby('City').size().reset_index(name = 'Remaining Count')

plt.bar(churn_city['City'], churn_city['Churn Count'])
plt.xlabel = 'City'
plt.ylabel = 'Count'
plt.tight_layout()
plt.show()


