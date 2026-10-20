# -*- coding: utf-8 -*-
"""
Predict Customer churn usding logistic regression
"""

##############################################################
# Import Data 
##############################################################

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Silence warnings
pd.set_option('future.no_silent_downcasting', True)

# Import and shuffle data
raw_data = pd.read_excel('telco_customer_churn.xlsx')
raw_data = shuffle(raw_data, random_state=42)

##############################################################
# Data Cleaning and Preparation
##############################################################

# Drop irrelevent columns and duplicate entries
raw_data.drop_duplicates(inplace=True)
desc = raw_data.describe()
raw_data.isna().sum() # only 'Churn Reason' - pass

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

##############################################################
# Feature Engineering
##############################################################

# Class balance - See how many customers churned and proportion of
raw_data["Churn Value"].value_counts()
raw_data["Churn Value"].value_counts(normalize = True)

num_vars = ["Total Charges"]
categorical_vars = ["Phone Service"]

# Select relevent features
X = raw_data.drop(["output"], axis = 1)
y = raw_data['Churn Value']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)
    ## !! Note on stratify for classification problems
    
from lin_regression import feature_eng

feature_eng(X_train, X_test, categorical_vars, num_vars)

##############################################################
# Logistic Classifier
##############################################################

# Instantiate classifier (clf) model object
clf = LogisticRegression(random_state = 42)

# Train our model
clf.fit(X_train, y_train)

# Assess model accuracy 
y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)

# get the probability of datapoint falling into 0 and 1 classes 
y_pred_prob = clf.predict_proba(X_test)

# Confusion Matrix (to assess accuracy)
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-v0_8-poster")
plt.matshow(conf_matrix, cmap = 'coolwarm')
plt.gca().xaxis.tick_bottom() # ticks from top of plot to bottom?
plt.title("Confusion Matrix")
plt.ylabel("Actual Class")
plt.xlabel("Predicted Class")

for (i, j), corr_value in np.ndenumerate(conf_matrix):
    plt.text(j, i, corr_value, ha = 'center', va = "center", fontsize = 20)
plt.show()

