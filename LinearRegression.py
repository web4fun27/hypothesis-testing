import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("/Users/mihai/Documents/GitHub/hypothesis-testing/alte fisiere/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()
#print(prod_per_year)

X = prod_per_year["year"]
X = X.values.reshape(-1, 1)
y = prod_per_year['totalprod']

plt.scatter(X, y)

#plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
print(regr.intercept_)

y_predict = regr.predict(X)

plt.plot(X, y_predict)
#plt.show()

X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

#print(X_future)

future_predict = regr.predict(X_future)

plt.plot(X_future, future_predict)
plt.show()

