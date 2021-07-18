import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Load the Boston housing dataset
from sklearn.datasets import load_boston
boston = load_boston()

# Transform dataset into a dataframe
df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

# Initialize the linear regression model
reg = linear_model.LinearRegression()

# Split the data into 67% training and 33% testing data
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=40)

# Train model
reg.fit(x_train, y_train)

# Predict values
y_pred = reg.predict(x_test)

# Print predictions and actual values
print(y_pred)
print(y_test)

# Check accuracy using Mean Squared Error (MSE)
print(np.mean(y_pred - y_test) ** 2)