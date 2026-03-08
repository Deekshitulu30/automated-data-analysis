import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Automated Data Analysis Tool")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Basic Info
    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Statistics
    st.subheader("Statistical Summary")
    st.write(df.describe())

    # Missing Values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Correlation
    st.subheader("Correlation Matrix")

    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

    # Histogram
    st.subheader("Histogram")

    column = st.selectbox("Select column", df.columns)

    fig2, ax2 = plt.subplots()
    df[column].hist(ax=ax2)

    st.pyplot(fig2)

    # Scatter plot
    st.subheader("Scatter Plot")

    col1 = st.selectbox("X-axis", df.columns)
    col2 = st.selectbox("Y-axis", df.columns)

    fig3, ax3 = plt.subplots()
    ax3.scatter(df[col1], df[col2])

    st.pyplot(fig3)