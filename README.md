# Time Series Forecasting

Course materials and exercises for the Time Series Forecasting class.

## Contents

### Time Series Exploration
- `class_1_data_aggregation.ipynb` - Data aggregation techniques for time series analysis  
- `class_2_time_patterns.ipynb` - Identifying and analyzing temporal patterns  
- `class_3_acf_pacf.ipynb` - Autocorrelation and partial autocorrelation functions  
  
- `smart_meter_data.csv` - Smart meter dataset 
- `UK_electricity_demand_2024.csv` - UK electricity demand dataset for the year 2024
- `AUS monthly beer production.csv`- quaterly beer production in Australia (1956-1995)
  

## Setup

### Prerequisites
- Python 3.8+
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

## Resources

### Books
- Hyndman & Athanasopoulos - *Forecasting: Principles and Practice* (OTexts, 2018)
  [Free online resources] (https://otexts.com/fpp3/)
- Nielsen - *Practical Time Series Analysis* (O'Reilly, 2019)
- Nield - *Essential Math for Data Science* (O'Reilly, 2022)

### Datasets
accessing datasets in **Python**:   
  *import statsmodels.api as sm *   
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

### Learning links
- [StatQuest](https://www.youtube.com/@statquest) - Statistics tutorials

## License

Course materials for educational purposes.
