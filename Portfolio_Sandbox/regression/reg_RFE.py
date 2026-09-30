import pandas as pd
import numpy as np
from sklearn.utils import shuffle

# Silence warnings
pd.set_option('future.no_silent_downcasting', True)

raw_data = pd.read_excel('telco_customer_churn.xlsx')

##############################################################
# Data Cleaning and Preparation
##############################################################

# Drop irrelevent columns and duplicate entries
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

# Drop the column for Tenure Months == 0 as there is no data associated with these customers yet
raw_data = raw_data[raw_data['Tenure Months'] != 0]

# Shuffle data
raw_data = shuffle(raw_data)

##############################################################
# Feature Engineering
##############################################################

'''split the data into training and test sets'''
from sklearn.model_selection import train_test_split

# Recode 'No internet service' / 'No phone service' to plain 'No' in the service type columns.
# Otherwise OneHotEncoding creates identical duplicate columns, which splits coefficients and confuses RFECV's ranking.
# That information is still captured once by 'Internet Service' and 'Phone Service'.
service_cols = ["Multiple Lines", "Online Security", "Online Backup", "Device Protection",
              "Tech Support", "Streaming TV", "Streaming Movies"]
raw_data[service_cols] = raw_data[service_cols].replace(
    {"No internet service": "No", "No phone service": "No"}
)

# Define feature sets and target
target = 'CLTV' 
categorical_vars = ['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service',
'Multiple Lines', 'Internet Service', 'Online Security',
'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV',
'Streaming Movies', 'Contract', 'Payment Method']
num_vars = ['Tenure Months', 'Monthly Charges', 'Total Charges']

# Select predictor features (X) and target (y)
X = raw_data[num_vars + categorical_vars].copy()
y = raw_data[target].copy()

# Train / Test Split (PREVENTS LEAKAGE)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

'''oneHotEncoder for categorical vars'''
from sklearn.preprocessing import OneHotEncoder, StandardScaler

one_hot_encoder = OneHotEncoder(sparse_output = False, drop = "first") 

X_train_encoded = one_hot_encoder.fit_transform(X_train[categorical_vars])
X_test_encoded = one_hot_encoder.transform(X_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

X_train_encoded = pd.DataFrame(X_train_encoded, columns = encoder_feature_names)
X_train = pd.concat([X_train.reset_index(drop=True), X_train_encoded.reset_index(drop = True)], axis = 1)
X_train.drop(categorical_vars, axis = 1, inplace = True)

X_test_encoded = pd.DataFrame(X_test_encoded, columns = encoder_feature_names)
X_test = pd.concat([X_test.reset_index(drop=True), X_test_encoded.reset_index(drop = True)], axis = 1)
X_test.drop(categorical_vars, axis = 1, inplace = True)

'''StandardScaler for numeric vars'''
scaler = StandardScaler()
X_train[num_vars] = scaler.fit_transform(X_train[num_vars])
X_test[num_vars] = scaler.transform(X_test[num_vars])

##############################################################
# Run RFECV 
##############################################################

from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression
# regression: output is numeric 

regressor = LinearRegression()
feature_selector = RFECV(regressor) # CV = 5 as default

fit = feature_selector.fit(X_train, y_train)

# how many variables is optimal?
optimal_feature_count = feature_selector.n_features_
print(f"Optimal number of feature: {optimal_feature_count}") # 2


X_new = X_test.loc[:, feature_selector.get_support()]
important_features = X_new.columns
print(important_features)

import matplotlib.pyplot as plt

# go from 0 to 4 features
plt.plot(range(1, len(fit.cv_results_['mean_test_score']) + 1), fit.cv_results_['mean_test_score'], marker = "o")
plt.ylabel("Model Score")
plt.xlabel("Number of Features")
plt.title(f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()

##############################################################
# Evaluate the Test Set
##############################################################

from sklearn.metrics import mean_squared_error, r2_score
sel_cols = X_train.columns[feature_selector.support_]
model = LinearRegression().fit(X_train[sel_cols], y_train)
y_pred_test = model.predict(X_test[sel_cols])
print("Test R2:", r2_score(y_test, y_pred_test))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_test)))

'''
Test R2: 0.15157187020655483
Test RMSE: 1081.2722163244134
'''

import lin_reg_plots as lrp

# lrp.plot_linear_performance(y_train, y_test, y_pred_train, y_pred_test, r2_train, r2_test)
lrp.plot_feature_importance(num_vars, encoder_feature_names, model)