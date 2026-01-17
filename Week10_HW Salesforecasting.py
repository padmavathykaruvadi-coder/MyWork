import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("Pastweeks/sales_data.csv")

print(data.describe())

X = data[["Advertising_Spend"]].values
y = data["Total Amount"].values

plt.scatter(X, y)
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.title("Advertising Spend vs Sales")
plt.show()

linear_model = LinearRegression()
linear_model.fit(X, y)
y_linear_pred = linear_model.predict(X)

linear_mse = mean_squared_error(y, y_linear_pred)
linear_rmse = np.sqrt(linear_mse)
linear_r2 = r2_score(y, y_linear_pred)

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_poly_pred = poly_model.predict(X_poly)

poly_mse = mean_squared_error(y, y_poly_pred)
poly_rmse = np.sqrt(poly_mse)
poly_r2 = r2_score(y, y_poly_pred)

comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Polynomial Regression (Degree 3)"],
    "MSE": [linear_mse, poly_mse],
    "R2_Score": [linear_r2, poly_r2]
})

print(comparison)

sorted_idx = np.argsort(X.flatten())
X_sorted = X[sorted_idx]

plt.scatter(X, y, label="Actual Data")
plt.plot(X_sorted, y_linear_pred[sorted_idx], label="Linear Regression")
plt.plot(X_sorted, y_poly_pred[sorted_idx], label="Polynomial Regression")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()

new_spend = float(input("Enter Advertising Spend value: "))
linear_prediction = linear_model.predict([[new_spend]])
poly_prediction = poly_model.predict(poly.transform([[new_spend]]))

print("Linear Regression Prediction:", linear_prediction[0])
print("Polynomial Regression Prediction:", poly_prediction[0])
