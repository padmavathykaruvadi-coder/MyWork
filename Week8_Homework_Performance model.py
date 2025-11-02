import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class StudentPerformanceModel:
    def __init__(self, csv_path="Student_Performance.csv", target_col="Performance Index", test_size=0.2, random_state=42):
        self.csv_path = csv_path
        self.target_col = target_col
        self.test_size = test_size
        self.random_state = random_state
        self.df = None
        self.feature_names = None
        self.model = LinearRegression()
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.y_pred = None

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)

    def preprocess(self):
        self.df = self.df.dropna()
        if self.target_col not in self.df.columns:
            raise ValueError(f"Target column '{self.target_col}' not found.")
        numeric_df = self.df.select_dtypes(include=[np.number])
        if self.target_col not in numeric_df.columns:
            raise ValueError("Target must be numeric.")
        self.feature_names = [c for c in numeric_df.columns if c != self.target_col]
        if not self.feature_names:
            raise ValueError("No numeric features found.")
        X = numeric_df[self.feature_names]
        y = numeric_df[self.target_col]
        return X, y

    def split(self, X, y):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        self.y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, self.y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, self.y_pred)
        print(f"MSE: {mse:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"R2: {r2:.4f}")

    def predict_user_input(self):
        print("\nEnter values for the following features:")
        vals = []
        for name in self.feature_names:
            while True:
                try:
                    v = float(input(f"{name}: ").strip())
                    vals.append(v)
                    break
                except ValueError:
                    print("Enter a numeric value.")
        arr = np.array(vals, dtype=float).reshape(1, -1)
        pred = self.model.predict(arr)[0]
        print(f"\nPredicted Performance Index: {pred:.2f}")

    def visualize(self):
        plt.figure()
        plt.scatter(self.y_test, self.y_pred)
        lims = [min(self.y_test.min(), self.y_pred.min()), max(self.y_test.max(), self.y_pred.max())]
        plt.plot(lims, lims)
        plt.xlabel("Actual Performance Index")
        plt.ylabel("Predicted Performance Index")
        plt.title("Actual vs Predicted")
        plt.show()

if __name__ == "__main__":
    spm = StudentPerformanceModel()
    spm.load_data()
    X, y = spm.preprocess()
    spm.split(X, y)
    spm.train()
    spm.evaluate()
    spm.predict_user_input()
    spm.visualize()
