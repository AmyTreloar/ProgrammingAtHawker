import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv("datasets/Data.csv")
#print(dataset)
x = dataset.iloc[ : , :-1].values
y = dataset.iloc[ : , 3].values

imputer = Imputer(missing_values="NaN", strategy="mean", axis = 0)
imputer = imputer.fit(x[ : , 1:3])
x[ : , 1:3] = imputer.transform(x[ : , 1:3])

labelencoder_x = LabelEncoder()
labelencoder_y = LabelEncoder()

x[ : , 0] = labelencoder_x.fit_transform(x[ : , 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()
y = labelencoder_y.fit_transform(y)


x_train, x_test, y_train, y_test = train_test_split( x , y , test_size = 0.2, random_state = 0)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)
print(x_train, y_train)


