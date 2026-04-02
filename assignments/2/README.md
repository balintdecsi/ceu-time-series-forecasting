# Final Project: UK Solar Electricity Forecasting (2021-2024)

## 🌟 Overview
In this project, I analyze and forecast solar electricity generation in the UK. Using a dataset covering 2021 to 2024, I explore temporal patterns, seasonal trends, and build a robust statistical model to predict future energy output. This is a critical task for grid stability and renewable energy management.

## 📊 Dataset & Preparation
- **Source**: `UK_electricity_solar_2021_2024.csv` (Expected at project root).
- **Granularity**: Half-hourly intervals.
- **Key Features**: `embedded_solar_generation`, `england_wales_demand`, capacity, and holiday indicators.
- **My Approach**: I aggregate the volatile half-hourly data into **daily sums**. This reduction in noise makes long-term seasonal patterns much clearer and improves the stability of my forecasting models.

## 🛠️ Technical Methodology & Decisions

### 1. Exploratory Data Analysis (EDA)
I use `ydata-profiling` to generate a comprehensive overview of the dataset. This allowed me to quickly identify the strong annual seasonality (peaking in summer, dipping in winter) and confirm the integrity of the solar generation values.

### 2. Statistical Testing
- **Stationarity**: I perform the Augmented Dickey-Fuller (ADF) test to check for unit roots. 
- **Decomposition**: Using `statsmodels`, I decompose the series into trend, seasonal, and residual components to validate the strength of the yearly cycle.
- **ACF/PACF**: I analyze autocorrelation plots to determine the appropriate AR and MA terms for my models.

### 3. Modeling: Why ARIMA?
I selected the **ARIMA(7, 1, 1)** model for several key reasons:
- **Differencing**: By setting `d=1`, the model handles non-stationarity internally, avoiding manual transformations that could lead to data leakage during the training/test split.
- **Seasonality**: An AR term of 7 captures the weekly dependencies often found in energy demand patterns that influence generation reporting.
- **Parsimony**: Compared to complex deep learning models, ARIMA provides a clear baseline and is computationally efficient for univariate forecasting.

### 4. Validation Strategy
I employ a **chronological split** (80% training, 20% testing). I do not use random shuffling, as preserving the temporal order is essential for realistic time series evaluation.

## 🚀 How to Run the Project

### Prerequisites
- [Python 3.10+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) (Recommended for lightning-fast environment setup)

### Setup & Execution

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/francescaconselvan/time_series_forecasting.git
    cd ceu-time-series-forecasting
    ```

2.  **Sync the environment**:
    ```bash
    # This installs all dependencies including jupyter and autogluon
    uv sync
    ```

3.  **Run the Notebook**:
    ```bash
    # Launch jupyter from the project root or assignment folder
    uv run jupyter notebook assignments/2/final_project.ipynb
    ```

## 📂 Project Structure (Assignment 2)
- `final_project.ipynb`: The main workflow containing EDA, modeling, and evaluation.
- `blog_post.md`: A non-technical summary of my findings and their real-world implications.
- `assets/`: Plots and visualizations generated during my analysis.

## 🤖 AI Declaration
I used [Gemini 3.1](https://gemini.google.com/) in Gemini CLI to develop the initial code skeleton and enhance the visual aesthetics of the project's charts. The tool was used to provide boilerplate logic for data processing and suggestions for matplotlib/seaborn styling, which I subsequently reviewed, refined, and integrated into the final notebook.

## 📈 Results Summary
My baseline ARIMA model achieved a Mean Absolute Error (MAE) of approximately 1245 MW. While the model captures the general seasonal trajectory, the high variance in weather-dependent generation suggests that future iterations could benefit from incorporating exogenous cloud cover data (SARIMAX).
