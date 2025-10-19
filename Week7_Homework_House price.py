import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = pd.read_csv("house_price_regression_dataset.csv")
cols = {c.lower().strip(): c for c in data.columns}

def pick(candidates):
    for key, orig in cols.items():
        if any(k in key for k in candidates):
            return orig
    raise KeyError(f"Could not find any of: {candidates} in columns {list(data.columns)}")

x_col = pick(["square", "sqft", "area"])
y_col = pick(["price", "amount", "cost"])

data = data[[x_col, y_col]].dropna().rename(columns={x_col: "Square Footage", y_col: "Price"})

plt.scatter(data["Square Footage"], data["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")
plt.show()

X = data[["Square Footage"]]
Y = data["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

order = np.argsort(X_test.values.reshape(-1))
plt.scatter(X_test, y_test, label="Actual")
plt.plot(X_test.values.reshape(-1)[order], y_pred[order], linewidth=2, label="Predicted Line")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Regression Line: Actual vs Predicted")
plt.legend()
plt.show()

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.show()