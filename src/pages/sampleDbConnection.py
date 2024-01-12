import streamlit as st
import mysql.connector

st.set_page_config(page_title='MySQL',page_icon=':bar_chart:',layout='wide')
st.title("Checking MySQL Connection")

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    password = "Experion@1972",
    database= "dwh_dashboard"
)

mycursor = mydb.cursor()
