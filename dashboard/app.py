import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Set up the dashboard page
st.set_page_config(
    page_title="Stock Price Prediction Dashboard",
    layout="wide"
)

# Dashboard title
st.title("S&P 500 Stock Price Prediction Dashboard")
st.write(
    "Explore historical stock prices and compare actual closing prices "
    "with predictions from Linear Regression and Random Forest models."
)

# Load prediction results
df = pd.read_csv(BASE_DIR / "stock_prediction_results.csv")

# Load original dataset containing technical indicators
indicators_df = pd.read_csv(BASE_DIR / "stock_data_with_indicators.csv.gz", compression="gzip")

# Convert date column to datetime
indicators_df["date"] = pd.to_datetime(indicators_df["date"])

# Filter indicators for selected company

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Display a confirmation
st.success("Prediction data loaded successfully!")

# Get the list of available company tickers
tickers = sorted(df["name"].unique())

# Create a dropdown for company selection
selected_ticker = st.selectbox(
    "Select a company ticker:",
    tickers
)

# Get technical indicators for selected company
indicator_data = indicators_df[
    indicators_df["name"] == selected_ticker
].copy()

indicator_data = indicator_data.sort_values("date")
# Filter data for the selected company
company_data = df[df["name"] == selected_ticker].copy()

# Date range filter
st.subheader("Select Date Range")

start_date = company_data["date"].min().date()
end_date = company_data["date"].max().date()

date_range = st.date_input(
    "Choose the date range:",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date
)

# Apply selected date range
if len(date_range) == 2:
    company_data = company_data[
        (company_data["date"].dt.date >= date_range[0]) &
        (company_data["date"].dt.date <= date_range[1])
    ]

# Display selected company
st.subheader(f"Stock Analysis: {selected_ticker}")

# Show number of records
st.write(f"Number of prediction records: {len(company_data)}")

# Dashboard summary metrics
if not company_data.empty:

    latest_price = company_data["close"].iloc[-1]
    average_price = company_data["close"].mean()
    total_records = len(company_data)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Latest Closing Price",
        f"${latest_price:.2f}"
    )

    col2.metric(
        "Average Closing Price",
        f"${average_price:.2f}"
    )

    col3.metric(
        "Trading Records",
        total_records
    )

# Historical closing price chart
st.subheader("Historical Closing Prices")

historical_chart = px.line(
    company_data,
    x="date",
    y="close",
    title=f"Historical Closing Price - {selected_ticker}",
    labels={
        "date": "Date",
        "close": "Closing Price ($)"
    }
)

st.plotly_chart(historical_chart, use_container_width=True)

# Actual vs Predicted Closing Prices
st.subheader("Actual vs. Predicted Closing Prices")

comparison_chart = px.line(
    company_data,
    x="date",
    y=["next_close", "linear_regression", "random_forest"],
    title=f"Actual vs Predicted Prices - {selected_ticker}",
    labels={
        "date": "Date",
        "value": "Stock Price ($)",
        "variable": "Price Type"
    }
)

st.plotly_chart(comparison_chart, use_container_width=True)

# Model performance metrics
st.subheader("Model Performance Comparison")

# Calculate Mean Absolute Error
lr_mae = (company_data["next_close"] - company_data["linear_regression"]).abs().mean()

rf_mae = (company_data["next_close"] - company_data["random_forest"]).abs().mean()

baseline_mae = (company_data["next_close"] - company_data["baseline"]).abs().mean()

# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric("Linear Regression MAE", round(lr_mae, 4))
col2.metric("Random Forest MAE", round(rf_mae, 4))
col3.metric("Baseline MAE", round(baseline_mae, 4))

# Technical Indicators
st.subheader("Technical Indicators")

# SMA chart
sma_chart = px.line(
    indicator_data,
    x="date",
    y="sma_5",
    title=f"5-Day Simple Moving Average - {selected_ticker}"
)

st.plotly_chart(sma_chart, use_container_width=True)

# RSI chart
rsi_chart = px.line(
    indicator_data,
    x="date",
    y="rsi_14",
    title=f"14-Day Relative Strength Index - {selected_ticker}"
)

st.plotly_chart(rsi_chart, use_container_width=True)
