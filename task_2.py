import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# -------------------------------
# 1. Load Time-Series Dataset
# -------------------------------
df = pd.read_csv(r"D:\codeveda\level-2\monthly_dates.csv", parse_dates=["date"], index_col="date")
print(df.head())

# -------------------------------
# 2. Plot Time Series
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(df["sales"])
plt.title("Monthly Sales Time Series")
plt.xlabel("date")
plt.ylabel("sales")
plt.grid()
plt.show()

# -------------------------------
# 3. Decompose Time Series
# -------------------------------
decomposition = seasonal_decompose(df["sales"], model="additive", period=7)

plt.figure(figsize=(12, 8))
decomposition.plot()
plt.show()

# -------------------------------
# 4. Moving Average Smoothing
# -------------------------------
df["MA_3"] = df["sales"].rolling(window=3).mean()     # 3-month moving average
df["MA_6"] = df["sales"].rolling(window=6).mean()     # 6-month moving average

# Plot smoothed series
plt.figure(figsize=(10, 6))
plt.plot(df["sales"], label="Original Data")
plt.plot(df["MA_3"], label="3-Month Moving Average")
plt.plot(df["MA_6"], label="6-Month Moving Average")
plt.title("Moving Average Smoothing")
plt.xlabel("date")
plt.ylabel("sales")
plt.legend()
plt.grid()
plt.show()
