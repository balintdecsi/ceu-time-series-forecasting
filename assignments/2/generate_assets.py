import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import os

# Set style
plt.rcParams['figure.figsize'] = (12, 6)
sns.set_theme(style='whitegrid')

# Create directory for assets if it doesn't exist
output_dir = 'assignments/2/assets'
os.makedirs(output_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv('UK_electricity_solar_2021_2024.csv', parse_dates=['settlement_date'], index_col='settlement_date')

# 1. Overview Plot
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['embedded_solar_generation'], color='orange', alpha=0.7)
plt.title('UK Solar Electricity Generation (2021-2024)')
plt.xlabel('Date')
plt.ylabel('Generation (MW)')
plt.tight_layout()
plt.savefig(f'{output_dir}/solar_generation_overview.png')
plt.close()

# Prepare daily data
df_daily = df.resample('D').mean(numeric_only=True)
df_daily.dropna(inplace=True)

# 2. Seasonal Decomposition
result = seasonal_decompose(df_daily['embedded_solar_generation'], model='additive', period=365)
fig = result.plot()
fig.set_size_inches(12, 10)
plt.tight_layout()
plt.savefig(f'{output_dir}/seasonal_decomposition.png')
plt.close()

# 3. ACF & PACF
fig, axes = plt.subplots(1, 2, figsize=(16, 5))
plot_acf(df_daily['embedded_solar_generation'], ax=axes[0], lags=40)
plot_pacf(df_daily['embedded_solar_generation'], ax=axes[1], lags=40)
axes[0].set_title('Autocorrelation (ACF)')
axes[1].set_title('Partial Autocorrelation (PACF)')
plt.tight_layout()
plt.savefig(f'{output_dir}/acf_pacf_plots.png')
plt.close()

# 4. ARIMA Forecast
train_size = int(len(df_daily) * 0.8)
train, test = df_daily.iloc[:train_size], df_daily.iloc[train_size:]

model = ARIMA(train['embedded_solar_generation'], order=(7, 1, 1))
results = model.fit()

forecast_obj = results.get_forecast(steps=len(test))
forecast_mean = forecast_obj.predicted_mean
conf_int = forecast_obj.conf_int()

plt.figure(figsize=(14, 6))
plt.plot(train.index[-180:], train['embedded_solar_generation'][-180:], label='Historical (last 6 months)', color='blue')
plt.plot(test.index, test['embedded_solar_generation'], label='Actual Test Data', color='gray', alpha=0.5)
plt.plot(test.index, forecast_mean, label='ARIMA Forecast', color='red')
plt.fill_between(test.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='red', alpha=0.1, label='95% Confidence Interval')
plt.title('UK Solar Generation: ARIMA Forecast vs Actuals')
plt.xlabel('Date')
plt.ylabel('Generation (MW)')
plt.legend()
plt.tight_layout()
plt.savefig(f'{output_dir}/arima_forecast.png')
plt.close()

print(f"Assets created in {output_dir}")
