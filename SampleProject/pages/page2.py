import streamlit as st
import mysql.connector

st.set_page_config(page_title='Page 2',page_icon=':bar_chart:',layout='wide')
st.title("This is Page 2")

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user= "root",
    password = "sachin@123",
    database= "dwh_dashboard"
)

mycursor = mydb.cursor()

print("Connection established")