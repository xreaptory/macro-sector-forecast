# macro-sector-forecast
Macro-suprise-driven sector rotation and country growth forecasting, from FRED/World Bank data to validated, backtested sector and stock predictions 

## Description
Project Description:

This project develops a machine learning framework for macroeconomic forecasting, with a focus on simulating market responses to crisis, political, and social shocks. The initiative draws on IMF datasets and statistical frameworks to build robust models linking global macroeconomic indicators to microeconomic sector dynamics.
for example, quantifying how shifts in monetary policy or geopolitical events propagate into smaller scale industry-specific outcomes such as Germany's automotive sector.

The methodology combines predictive machine learning, sentiment analysis of news and policy communications, and statistical/econometric analysis to model transmission mechanisms between macro-level shocks and sector-level responses. FRED's time series data (interest rates, GDP, trade balances, industrial production, employment, etc.) will serve as a core input for training and validating these models, alongside IMF data sources, enabling cross-country and cross-sector comparative analysis.

Intended use: Programmatic access to retrieve historical and updated economic time series via the FRED API for model training, backtesting, and real-time forecasting pipelines.

## dependencies 

- Python 3.11+
- Venv
- sdmx1 (python lib)
- msal (python lib)
- requests (python lib)

## Setup

- setup venv
    - python -m venv .venv
    - ./.venv/bin/activate.ps1/bat/ etc ...
- install deps
    - pip install sdmx1
    - pip install msal