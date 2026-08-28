'''
Barebones structure of training and validating a model in scikit learn
'''

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data_for_model = pd.read_csv("data_for_model.csv")

X = data_for_model[["input_var1", "input_var2", "input_var3"]]
y = data_for_model["output_var"]

# in this example, wasnt 20% of data in test set and 80 in training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# shell of object, specify class
regressor = LinearRegression()

# train the model with 'fit'
regressor.fit(X_train, y_train)

# Use the predict method to apply the trained model to the test set input variables to get predictions for the outputs
y_pred = regressor.predict(X_test)

# Evaluate the accuracy of the model based on the difference 
    # between predicted output values and actual output values 
    # for the test set
print(r2_score(y_test, y_pred))



