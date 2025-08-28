import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="centered"
)


# --- Data Loading and Cleaning ---
# This function loads data and handles duplicates. Caching makes it faster.
@st.cache_data
def load_data():
    try:
        # Load the dataset
        df = pd.read_csv('employe (1).csv')
        # Drop duplicates as you did in your notebook
        df.drop_duplicates(inplace=True)
        return df
    except FileNotFoundError:
        st.error("Error: 'employe (1).csv' not found. Make sure it's in the same folder.")
        return None

df = load_data()

# Only proceed if the data was loaded successfully
if df is not None:
    # --- Website Content ---

    st.title("📊 HR Attrition Analytics")
    st.write(
        "This dashboard explores the factors that lead to employee attrition, based on the 'People Charm' case study."
    )

    # Show a small sample of the data
    if st.checkbox("Show raw data sample"):
        st.dataframe(df.head())

    # --- Visualizations ---

    # Plot 1: Number of Projects vs. Attrition
    st.header("How does the number of projects affect attrition?")
    st.write(
        "Employees with only 2 projects or those overloaded with 6-7 projects have the highest attrition rates. A moderate workload (3-5 projects) seems ideal for retention."
    )
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='numberOfProjects', hue='left', ax=ax1)
    ax1.set_title("Number of Projects vs. Employee Attrition")
    ax1.set_xlabel("Number of Projects")
    ax1.set_ylabel("Number of Employees")
    st.pyplot(fig1)

    # Plot 2: Average Monthly Hours vs. Attrition
    st.header("How do average monthly hours relate to attrition?")
    st.write(
        "Attrition is highest among employees who are either underworked (<150 hours/month) or significantly overworked (>250 hours/month)."
    )
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x='avgMonthlyHours', hue='left', bins=15, multiple="stack")
    ax2.set_title("Average Monthly Hours vs. Employee Attrition")
    ax2.set_xlabel("Average Monthly Hours")
    ax2.set_ylabel("Number of Employees")
    st.pyplot(fig2)

    # Plot 3: Promotions vs. Attrition
    st.header("Does promotion in the last 5 years impact attrition?")
    st.write(
        "Overwhelmingly, employees who have not received a promotion in the last 5 years are the ones leaving the company."
    )
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='promotionInLast5years', hue='left', ax=ax3)
    ax3.set_title("Promotion in Last 5 Years vs. Employee Attrition")
    ax3.set_xlabel("Promotion in Last 5 Years (0=No, 1=Yes)")
    ax3.set_ylabel("Number of Employees")
    st.pyplot(fig3)