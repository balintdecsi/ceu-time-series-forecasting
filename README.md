# Time Series Forecasting

Course materials and exercises for the Time Series Forecasting class.

## Contents

### Time Series Exploration
- `class_1_data_aggregation.ipynb` - Data aggregation techniques for time series analysis
- `class_2_time_patterns.ipynb` - Identifying and analyzing temporal patterns
- `class_3_acf_pacf.ipynb` - Autocorrelation and partial autocorrelation functions

### Time Series Forecasting
- `4_ARIMA.ipynb` - ARIMA model for time series forecasting (stationarity, ACF/PACF, model fitting)
- `5_AutoGluon.ipynb` - AutoML time series forecasting with AutoGluon

### Datasets
- `smart_meter_data.csv` - Smart meter dataset (half-hourly electricity consumption)
- `UK_electricity_demand_2024.csv` - UK electricity demand dataset for the year 2024
- `AUS quaterly beer production.csv` - Quarterly beer production in Australia (1956-2010)
- `AUS monthly beer production.csv` - Monthly beer production in Australia (1956-2010)
  
  

## Setup

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/francescaconselvan/time_series_forecasting.git
cd time_series_forecasting
pip install -r requirements.txt
jupyter notebook
```

### Required Packages

- pandas - Data manipulation and analysis
- numpy - Numerical computing
- matplotlib - Data visualization
- seaborn - Statistical data visualization
- plotly - Interactive visualizations
- jupyter - Notebook environment
- statsmodels - Statistical models and time series analysis
- pmdarima - Auto ARIMA parameter selection
- scikit-learn - Machine learning metrics and utilities
- autogluon.timeseries - AutoML for time series forecasting
- ydata-profiling - Automated exploratory data analysis

## Resources

### Datasets
accessing datasets in **Python**:   
  *import statsmodels.api as sm*   
  Common time series datasets in statsmodels:  
  sunspots - Monthly sunspot data  
  co2 - Atmospheric CO2 concentrations  
  nile - Annual Nile river flow  
  macrodata - US macroeconomic data  
  elnino - Sea surface temperature data

  Python doesn't have as extensive built-in time series datasets, it also possible to access **R datasets** directly  
  *from statsmodels.datasets import get_rdataset*  

  Directly from **websites**:  
  - [UCI Machine Learning Repository](https://archive.ics.uci.edu/) - Time series datasets
  - [NOAA NAtional Centers for Enviromental Information](https://perma.cc/EA5R-TP5L) - US timeseries data related to temperature and precipitation

## License

Course materials for educational purposes.
