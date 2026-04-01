Mid-Course Exercise
Deadline: January 30, 2026

Choose one of the two datasets (AirPassengers.csv or donations.csv) and complete all tasks below. For those who also want to practice data cleaning and data transformation, you can use the London hourly profile dataset (saved in Parquet format)

Task 1: Exploratory Data Analysis (EDA)
Perform an exploratory data analysis on your chosen dataset. You may use any available Python library for EDA - here a selected list.

If you are using the London dataset (electricity profile), you have the extra task of data cleaning and data transformation

Task 2: Time Series Data Preparation
•	Convert the date/timestamp column to a datetime object (AirPassengers.csv has Date; donations.csv has timestamp)
•	Extract time components from the date/timestamp column:
      - Year
      - Month (numeric)
      - Month name
      - Week of the year

Task 3: Data Visualization
Create visualizations to explore patterns in the data:
•	Line plots at different levels of granularity (yearly, monthly, weekly aggregations)
•	Histogram showing the distribution of the target variable (passengers or donation amounts)

Task 4: Seasonal Decomposition
•	Perform seasonal decomposition using an appropriate Python package (e.g., statsmodels.tsa.seasonal.seasonal_decompose)
•	Visualize the trend, seasonal, and residual components
•	Determine an appropriate seasonal period for your dataset



Task 5: Autocorrelation and Partial Autocorrelation
Explore the autocorrelation function (ACF) and partial autocorrelation function (PACF) under different scenarios:
•	Original data: Plot ACF and PACF for the original (non-stationary) time series
•	Stationary data: Transform the data to make it stationary using differencing or other methods, then plot ACF and PACF
•	Before plotting ACF and PACF for the stationary data, verify stationarity using the Augmented Dickey-Fuller (ADF) unit root test
•	Compare and interpret the differences between the stationary and non-stationary ACF/PACF plots

Remember: The more lags you use, the lower the correlation will be. More recent periods typically have more impact on current values.

Example questions to explore:
      - How correlated is this month's value with last month's value?
      - How correlated is this month's value with the same month last year?

Task 6: Insights and Conclusions
Write your insights in a markdown cell addressing:
•	Key patterns and trends identified in the data
•	Seasonal patterns and their strength
•	Stationarity of the data and what transformations were needed
•	Autocorrelation findings and their implications for time series modelling
•	Any other interesting observations or anomalies discovered during the analysis


Submission Requirements
•	Format: Submit a Jupyter Notebook (.ipynb) with all code, visualizations, and markdown insights
•	Visualizations: All plots should be clearly labelled with titles, axis labels, and legends where appropriate
•	Deadline: January 30, 2026
