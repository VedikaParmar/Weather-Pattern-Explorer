import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\prmrv\Downloads\monthly_weather_data_2023_2025.csv", encoding='cp1252')

print(data)


# Create subplots: Temperature and Humidity
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Plot 1: Average Temperature
axs[0].plot(data['Month'], data['Avg Temperature'], color='red', label='Avg Temperature')
axs[0].set_ylabel('Temp (°C)')
axs[0].legend(loc='upper left')
axs[0].set_title("Monthly Weather Data")

# Plot 2: Humidity
axs[1].plot(data['Month'], data['Humidity'], color='blue', label='Humidity')
axs[1].set_ylabel('Humidity (%)')
axs[1].legend(loc='upper left')
axs[1].set_xlabel('Month')

plt.show()
