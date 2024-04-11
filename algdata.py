import pandas as pd
import matplotlib.pyplot as plt

# Load utility bill data
utility_bills = pd.read_csv('Data.csv')

# Convert date column to datetime format
utility_bills['Date'] = pd.to_datetime(utility_bills['Date'])

# Set 'Date' column as index
utility_bills.set_index('Date', inplace=True)

# Resample monthly and sum to get total utility consumption per month
monthly_consumption = utility_bills.resample('M').sum()

# Plot monthly consumption
plt.figure(figsize=(10, 6))
plt.plot(monthly_consumption.index, monthly_consumption['Electricity'], label='Electricity')
plt.plot(monthly_consumption.index, monthly_consumption['Gas'], label='Gas')
plt.plot(monthly_consumption.index, monthly_consumption['Water'], label='Water')
plt.title('Monthly Utility Consumption')
plt.xlabel('Date')
plt.ylabel('Consumption')
plt.legend()
plt.grid(True)
plt.show()