import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

# Silence warnings
pd.set_option('future.no_silent_downcasting', True)

raw_data = pd.read_excel('telco_customer_churn.xlsx')

######################################################
# Phase 1: Data Cleaning & Feature Engineering
######################################################

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

######################################################
# Phase 2: Regression with Demographic and Tenure Data
######################################################

'''split the data into training and test sets'''
from sklearn.model_selection import train_test_split, cross_val_score, KFold

services = ['Phone Service', 'Online Security', 'Online Backup', 'Device Protection', 
              'Tech Support', 'Streaming TV', 'Streaming Movies']

# Creates a True/False column for 'Yes' values and sums across rows (axis=1)
raw_data['# of Services'] = (raw_data[services] == 'Yes').sum(axis=1)

# Define feature sets and target
target = 'CLTV' 
categorical_vars = ['Dependents', 'Gender', 'Senior Citizen', 'Partner']
num_vars_p2 = ['Tenure Months', '# of Services']
# num_vars_p3 = ['Tenure Months', 'Number of Services', 'Monthly Charges', 'Total Charges']
# categorical_vars_p3 = ['Dependents', 'Gender', 'Senior Citizen', 'Partner', 'Contract', 'Payment Method']

# Select predictor features (X) and target (y)
X = raw_data[num_vars_p2 + categorical_vars].copy()
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
X_train[num_vars_p2] = scaler.fit_transform(X_train[num_vars_p2])
X_test[num_vars_p2] = scaler.transform(X_test[num_vars_p2])

######################################################
# Apply Linear Regression
######################################################

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

######################################################
# Model Assessment
######################################################
'''simple'''
from sklearn.metrics import r2_score, mean_squared_error

# STEP 4: Evaluate
y_pred_train = regressor.predict(X_train)
y_pred_test = regressor.predict(X_test)

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))

print(f"Train R²: {r2_train:.4f}")
print(f"Test R²: {r2_test:.4f}")
print(f"Test RMSE: ${rmse_test:.2f}")

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