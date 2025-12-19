import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("outputs/retail_pharmacy_analytics.csv")

st.set_page_config(page_title="Pharmacy Retail Intelligence", layout="wide")

st.title("💊 Pharmacy Retail Intelligence Dashboard")

st.metric("Total Medicines", df.shape[0])
st.metric("Average Profit", round(df['profit'].mean(), 2))

st.subheader("🔥 Top 10 Profitable Medicines")
st.dataframe(
    df[['medicine_name', 'profit']]
    .sort_values(by='profit', ascending=False)
    .head(10)
)

st.subheader("⚠️ High Expiry Risk Medicines")
st.dataframe(
    df[df['expiry_risk'] == 'High Risk']
    [['medicine_name', 'days_to_expiry', 'purchase_price']]
)
