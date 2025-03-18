import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("Python Data Dashboard")
st.write("Upload a CSV file to explore and visualize your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    st.success("File uploaded successfully.")

    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    if numeric_columns:
        st.subheader("Data Visualization")

        selected_column = st.selectbox("Choose a column", numeric_columns)

        chart_type = st.radio("Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

        if chart_type == "Bar Chart":
            fig = px.bar(df, x=df.index, y=selected_column, title=f"{selected_column} - Bar Chart")
        elif chart_type == "Line Chart":
            fig = px.line(df, x=df.index, y=selected_column, title=f"{selected_column} - Line Chart")
        elif chart_type == "Pie Chart":
            fig = px.pie(df, names=selected_column, title=f"{selected_column} - Pie Chart")

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No numeric columns found for visualization.")

else:
    st.info("Please upload a CSV file to begin.")
