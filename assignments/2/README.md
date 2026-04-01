# Final Project: UK Solar Electricity Forecasting

## Overview
This repository contains the final project for the Time Series course. The goal is to analyze the UK solar electricity generation dataset (2021-2024) and build a robust forecasting model using ARIMA/SARIMAX. 

## Dataset
- **Source:** Local dataset (`UK_electricity_solar_2021_2024.csv`)
- **Features:** Half-hourly interval data containing `embedded_solar_generation`, `england_wales_demand`, capacity, and holiday indicators.
- Note: The dataset should be located two directories above this one (`../../UK_electricity_solar_2021_2024.csv`).

## Files
- `final_project.ipynb`: Jupyter notebook containing all EDA, modeling, and forecasting code.
- `requirements.txt`: Python dependencies required to run the code.
- `blog_post.md`: Draft for the Medium blog post.

## Instructions to Run
1. Ensure `uv` is installed.
2. Install the requirements and sync the environment: `uv sync`
3. Launch Jupyter and open `final_project.ipynb`: `uv run jupyter notebook`
4. Run all cells in order.