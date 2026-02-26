import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Setup
st.set_page_config(page_title="Simple Kraljic Dashboard")
st.title("Kraljic Matrix Dashboard")

# 2. Load Data
df = pd.read_csv('realistic_kraljic_dataset.csv')

# 3. Sidebar Filter
region = st.sidebar.selectbox("Select Region", options=['All'] + list(df['Supplier_Region'].unique()))
if region != 'All':
    df = df[df['Supplier_Region'] == region]

# 4. Create the Matrix (Scatter Plot)
fig = px.scatter(
    df, 
    x="Supply_Risk_Score", 
    y="Profit_Impact_Score",
    color="Kraljic_Category",
    hover_name="Product_Name",
    title="Supply Risk vs Profit Impact"
)

# Add quadrant lines for easier reading
fig.add_hline(y=3, line_dash="dot")
fig.add_vline(x=3, line_dash="dot")

# 5. Display Chart and Data
st.plotly_chart(fig)

st.subheader("Product List")
st.dataframe(df)