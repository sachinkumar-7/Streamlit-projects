import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='PMO Dashboard',page_icon=':bar_chart:',layout='wide')

st.title("PMO Dashboard")
# uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx, csv,text')


df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows= 3,
    usecols='B:R',
    nrows=1000,
)
# st.dataframe(df)

#-----Sidebar-------

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)
customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)
gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)
# st.dataframe(df_selection)

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# Total KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sales_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sales_by_transaction}")
st.markdown("---")

# SALES BY PRODUCT LINE [BAR CHART]

sales_by_product_line = (
    df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

st.plotly_chart(fig_product_sales)