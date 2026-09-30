##############################################################
# Import Data 
##############################################################

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
from sklearn.model_selection import train_test_split, cross_val_score, KFold

# Recode 'No internet service' / 'No phone service' to plain 'No' in the service type columns.
# Otherwise OneHotEncoding creates identical duplicate columns, which splits coefficients and confuses RFECV's ranking.
# That information is still captured once by 'Internet Service' and 'Phone Service'.
service_cols = ["Multiple Lines", "Online Security", "Online Backup", "Device Protection",
              "Tech Support", "Streaming TV", "Streaming Movies"]
raw_data[service_cols] = raw_data[service_cols].replace(
    {"No internet service": "No", "No phone service": "No"}
)

# Agg Number of Services into DataFrame 

services = ['Phone Service', 'Online Security', 'Online Backup', 'Device Protection', 
              'Tech Support', 'Streaming TV', 'Streaming Movies']

# Creates a True/False column for 'Yes' values and sums across rows (axis=1)
raw_data['Number of Services'] = (raw_data[services] == 'Yes').sum(axis=1)

# Define feature sets and target
target = 'CLTV'

# # Feature Set 1:
# feat_set = 'Feature Set 1'
# categorical_vars = ['Dependents', 'Gender', 'Senior Citizen', 'Partner']
# num_vars = ['Tenure Months']

# # Feature set 2:
# feat_set = 'Feature Set 2'
# categorical_vars = ['Dependents', 'Gender', 'Senior Citizen', 'Partner']
# num_vars = ['Tenure Months', 'Number of Services']

# Feature set 3
feat_set = 'Feature Set 3'
num_vars = ['Tenure Months', 'Number of Services']
categorical_vars = ['Dependents', 'Gender', 'Senior Citizen', 'Partner', 'Contract', 'Payment Method']

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
# Apply Linear Regression
##############################################################

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

##############################################################
# Model Assessment
##############################################################
'''simple'''
from sklearn.metrics import r2_score, mean_squared_error

# STEP 4: Evaluate
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))

print(feat_set)
print(f"Train R²: {r2_train:.4f}")
print(f"Test R²: {r2_test:.4f}")
print(f"Test RMSE: ${rmse_test:.2f}")

'''
Train R²: 0.1566
Test R²: 0.1595
Test RMSE: $1075.79
'''

# translate results

import lin_reg_plots as lrp

lrp.plot_linear_performance(y_train, y_test, y_pred_train, y_pred_test, r2_train, r2_test)
lrp.plot_feature_importance(num_vars, encoder_feature_names, regressor)

'''from course'''

# Predict on the Test Set
y_pred = regressor.predict(X_test)

# Calculate R-Squared
r_squared = r2_score(y_test, y_pred)
print(r_squared)

# Cross Validation
cv = KFold(n_splits = 4, shuffle = True)
cv_scores = cross_val_score(regressor, X_train, y_train, cv = cv, scoring = "r2")
cv_scores.mean()

# Calculate adjusted R-Squared
num_data_points, num_input_vars = X_test.shape
adjusted_r_squared = 1 - (1 - r_squared) * (num_data_points - 1) / (num_data_points - num_input_vars - 1)
print(adjusted_r_squared)

# Extract Model Coefficients
coefficients = pd.DataFrame(regressor.coef_)
input_variable_names = pd.DataFrame(X_train.columns)
summary_stats = pd.concat([input_variable_names,coefficients], axis = 1)
summary_stats.columns = ["input_variable", "Coefficient"]

# Extract Model Intercept
regressor.intercept_

'''unstandardize data to get a monthly coefficient for business interests '''


##############################################################
# Check Results
##############################################################
# 1. Double-check your data preprocessing
print("CLTV statistics:")
print(y_test.describe())

print("\nTenure statistics (after standardization):")
print(X_train_combined['Tenure Months'].describe())

# 2. Check if there are missing values
print("\nMissing values in features:")
print(X_train_combined.isnull().sum())

# 3. Verify your one-hot encoding worked
print("\nFeatures in model:")
print(X_train_combined.columns.tolist())


##############################################################
# Compare Final Results of All Parts
##############################################################

## Loop, plots in functions, interpret results
# Part 1 (demographic + tenure)
print("PART 1 - Demographic & Tenure")
print(f"Test R²: {r2_test_part1:.4f}, RMSE: ${rmse_test_part1:.2f}\n")

# Part 2 (+ services)
print("PART 2 - Add Services")
print(f"Test R²: {r2_test_part2:.4f}, RMSE: ${rmse_test_part2:.2f}\n")

# Part 3 (+ contract/payment)
print("PART 3 - Add Contract & Payment")
print(f"Test R²: {r2_test_part3:.4f}, RMSE: ${rmse_test_part3:.2f}\n")

# Analysis
improvement_2_to_1 = r2_test_part2 - r2_test_part1
improvement_3_to_2 = r2_test_part3 - r2_test_part2
print(f"Part 2 improvement: +{improvement_2_to_1:.4f}")
print(f"Part 3 improvement: +{improvement_3_to_2:.4f}")