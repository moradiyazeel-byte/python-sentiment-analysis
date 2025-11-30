import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv(r"D:\codeveda\level-2\Book2.csv")
print("Dataset:\n", df.head())

# -------------------------------
# 2. Select Features & Target
# -------------------------------
X = df[["Experience", "Age"]]   # Independent variables
y = df["Salary"]                # Dependent variable

# -------------------------------
# 3. Split Data (Train 80% - Test 20%)
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# -------------------------------
# 4. Train Linear Regression Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# 5. Model Coefficients
# -------------------------------
print("\nIntercept (b0):", model.intercept_)
print("Coefficients (b1,b2):", model.coef_)

# -------------------------------
# 6. Predictions
# -------------------------------
y_pred = model.predict(X_test)

print("\nActual Salary:   ", np.array(y_test))
print("Predicted Salary:", np.array(y_pred))

# -------------------------------
# 7. Evaluation Metrics
# -------------------------------
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\nR-squared:", r2)
print("Mean Squared Error:", mse)
