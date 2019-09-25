import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('datasets/studentscores.csv')
x = dataset.iloc[ : , : 1].values
y = dataset.iloc[ : , 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/4, random_state = 0)

regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)

y_prediction = regressor.predict(x_test)

plt.scatter(x_train , y_train, color = 'red')
plt.plot(x_train , regressor.predict(x_train), color ='blue')
plt.scatter(x_test, y_test, color='green')
plt.plot(x_test, regressor.predict(x_test), color="yellow")
plt.show()
print("stuff")