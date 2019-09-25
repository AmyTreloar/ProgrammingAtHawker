import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("datasets/50_Startups.csv")
x = dataset.iloc[ : , : -1].values
y = dataset.iloc[ : , 4].values

labelencoder = LabelEncoder()
x[: , 3] = labelencoder.fit_transform(x[: ,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()

x = x[:, 1:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(x_train)
print(y_pred)