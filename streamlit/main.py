import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.header("House Value Prediction System")
st.subheader(
    "A Project Developed For Hack This Fall 3.0 By Team Sinister Bytes")


tab1, tab2, tab3 = st.tabs(
    ["EDA & Data Preprocessing", "Data Analysis", "Data Visualization"])
with tab1:
    st.header("Raw Data")
    df = pd.read_csv("../CSV/House Price.csv")
    st.write(df)
    st.header("Problems in Data Set")
    st.subheader("Outliers in Target Variable Sales Price")
    image = Image.open('outlierbefore.png')
    st.image(image, caption="Before")
    image = Image.open('outlierafter.png')
    st.image(image, caption="After")
    st.subheader("Simple mean regression")
    image = Image.open('mean.png')
    st.image(image)
    st.subheader("Simple mean regression with Grade ")
    image = Image.open('mean_grade.png')
    st.image(image)
with tab2:
    st.subheader("Scatter Plot for Trained Data")
    image = Image.open('scatter plot.png')
    st.image(image)
    st.subheader("Prediction Line ")
    image = Image.open('threadline.png')
    st.image(image)
    st.subheader("Sales Vs Count")
    image = Image.open('salesvcount.png')
    st.image(image)

with tab3:
    st.subheader("Factors affecting Area of House")
    image = Image.open('Areahouse.png')
    st.image(image)
    st.subheader("Conditions of House")
    image = Image.open('Conditionhouse.png')
    st.image(image)
    st.subheader("Effects of Renovation")
    image = Image.open('effect of renovation.png')
    st.image(image)
    st.subheader("Number of Amenities")
    image = Image.open('no.ofaminties.png')
    st.image(image)
