# Customer Purchase Prediction using Logistic Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# -------------------------------
# Step 1: Data Loading & Exploration
# -------------------------------
df = pd.read_csv("Pastweeks/sales_data.csv")

print("First 5 rows:\n", df.head())
print("\nDataset Shape:", df.shape)
print("\nSummary Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# -------------------------------
# Step 2: Feature & Target Selection (FIXED ✅)
# -------------------------------
# Create target variable since Purchased column does not exist
# Business logic: High total amount = Purchased
df['Purchased'] = df['Total Amount'].apply(lambda x: 1 if x > 500 else 0)

# Select features that ACTUALLY exist in your dataset
X = df[['Age', 'Advertising_Spend']]
y = df['Purchased']

# -------------------------------
# Step 3: Train-Test Split (80-20)
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Step 4: Logistic Regression Model
# -------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# -------------------------------
# Step 5: Model Evaluation
# -------------------------------
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\nConfusion Matrix:\n", cm)
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))

# -------------------------------
# Step 6: Confusion Matrix Visualization
# -------------------------------
plt.figure(figsize=(6, 4))
plt.imshow(cm, cmap='Blues')
plt.title("Confusion Matrix")
plt.colorbar()
plt.xticks([0, 1], ['Not Purchased', 'Purchased'])
plt.yticks([0, 1], ['Not Purchased', 'Purchased'])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha='center', va='center')

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.show()

# -------------------------------
# Step 7: User Input Prediction (FIXED ✅)
# -------------------------------
age = int(input("Enter Age: "))
ad_spend = int(input("Enter Advertising Spend: "))

input_data = [[age, ad_spend]]
probability = model.predict_proba(input_data)[0][1]
prediction = model.predict(input_data)[0]

print("\nPurchase Probability:", round(probability, 2))
print("Final Prediction:", "Yes" if prediction == 1 else "No")

# -------------------------------
# Step 8: Interpretation (Comments)
# -------------------------------
# Logistic Regression is suitable because the target variable is binary.
# Precision indicates how many predicted buyers actually purchased.
# Recall indicates how many actual buyers were correctly identified.
# High precision but low recall means predictions are accurate,
# but many potential buyers are missed.
