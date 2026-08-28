######################################################
# Feature Selection
######################################################

import pandas as pd

data_for_model = pd.read_excel('data_for_model.xlsx')

######################################################
# Phase 1: Data Cleaning & Feature Engineering
######################################################

'''
UL: update later
'''

# insert questions to ask yourself
data_for_model.describe()
data_for_model.isna().sum()

# raw_data['Total Charges'].dtype # O indicates that it's MIXED!
# raw_data['Total Charges'].map(type).value_counts()

# KNNInputer to fill in Nan? (is this before we split the data??)

######################################################
# Phase 2: Train the model to reduce noise
######################################################

'''
UL: Prevent data leakage by splitting the data... ML Need better explanation for notes
'''

from sklearn.model_selection import train_test_split

# Define feature sets and target
target = 'Churn Value'

# Select predictor features (X) and target (y) 
    # in this example, we use all non-target variables for training
X = data_for_model.drop([target], axis = 1)
y = data_for_model[target]

'''
Could also split into categorical / non data for later processing:
categorical_vars = [""]
cols_2_standardize = ['', '', '']

X = raw_data[cols_2_standardize + categorical_vars]
y = raw_data[target]
'''

# Train / Test Split (PREVENTS LEAKAGE)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

######################################################
# OneHotEncoder Example
######################################################

categorical_vars = ['']

from sklearn.preprocessing import OneHotEncoder

# Instantiate class; specify <drop = 'first'> to avoid the dummy variable trap!
one_hot_encoder = OneHotEncoder(sparse_output = False, drop = 'first') 

'''**FIT & TRANSFORM on Training set ONLY**
    # The encoder learns category names strictly from X_train
'''

X_train_encoded_array = one_hot_encoder.fit_transform(X_train[categorical_vars])

# Assign the new binary nparrays their original column names (excluding the 'first' dropped column)
encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

# Convert numpy array back into a pandas DataFrame using X_train's index
X_train_catagorical = pd.DataFrame(
    X_train_encoded_array, 
    columns=encoder_feature_names, 
    index=X_train.index
)

'''TRANSFORM ONLY on Test set
    # Uses category rules learned from X_train (No .fit() here!)
'''

X_test_encoded_array = one_hot_encoder.transform(X_test[categorical_vars])

X_test_catagorical = pd.DataFrame(
    X_test_encoded_array, 
    columns=encoder_feature_names, 
    index=X_test.index
)

######################################################
# StandardScaler Example
######################################################

cols_2_standardize = ['']

from sklearn.preprocessing import StandardScaler

# Instantiate Scaler
scale_standard = StandardScaler()

# apply the fit method to apply the rules of scaling 
# and then transform method to apply the scaling method to our data

'''**FIT & TRANSFORM on Training set ONLY**
    # Scaler calculates mean & std dev from X_train and rescales the numbers
'''
    
scaled_train_array = scale_standard.fit_transform(X_train[cols_2_standardize])

# Create a clean DataFrame for scaled training numerics
X_train_num = pd.DataFrame(
    scaled_train_array,
    columns=[f"{col} Standardized" for col in cols_2_standardize],
    index=X_train.index
)

'''TRANSFORM ONLY on Test set
    # Scales X_test using the mean & std dev saved from X_train (No .fit() here!)
'''

scaled_test_array = scale_standard.transform(X_test[cols_2_standardize])

# Create a clean DataFrame for scaled test numerics
X_test_num = pd.DataFrame(
    scaled_test_array,
    columns=[f"{col} Standardized" for col in cols_2_standardize],
    index=X_test.index
)

######################################################
## Combine Encoded and Scaled Features to a single modeling dataset 
######################################################

# Merge scaled numerics and encoded categoricals for Training set
X_train_final = pd.concat([X_train_num, X_train_catagorical], axis=1)

# Merge scaled numerics and encoded categoricals for Test set
X_test_final = pd.concat([X_test_num, X_test_catagorical], axis=1)