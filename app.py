import pandas as pd
import streamlit as st
import plotly
import plotly.express as px
import numpy as np
import openpyxl

## --load dataframe

# Contents of ~/my_app/streamlit_app.py
import streamlit as st

# Page
def page1():
    st.markdown("Chinese Indices")
    #st.sidebar.markdown("# Data Distribution")

def page2():
    st.markdown("SHIBOR")
    #st.sidebar.markdown("Filter️")

def page3():
    st.markdown("Macro Leverage Ratio")
    #st.sidebar.markdown("Filter️")

def page4():
    st.markdown("National Enterprise Index")
    #st.sidebar.markdown("Filter️")

def page5():
    st.markdown("Tax Income")

page_names_to_funcs = {
    "Chinese Indices": page1,
    "SHIBOR": page2,
    "Macro Leverage Ratio":page3,
    "National Enterprise Index":page4,
    "Tax Income":page5
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

# Page 1
if selected_page == "Chinese Indices":

    df = pd.read_csv('Chinese Indices.csv')
    df = df.dropna()

    # df = px.data.stocks()
    fig = px.line(df, x="Date", y=df.columns,
                  hover_data={"Date": "|%B %d, %Y"},
                  title='Chinese Indices')

    fig
    st.markdown(
    """
    Important Chinese Daily Macroeconomic Indices/Indicators from 09/27/2005 to 05/13/2022
    """
    )

# Page 2

if selected_page == "SHIBOR":

    df = pd.read_csv('SHIBOR.csv')
    df = df.dropna()

    # df = px.data.stocks()
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='SHIBOR')

    fig
    st.markdown(
    """
    Annualized SHIBOR (Shanghai Interbank Offered Rate) daily rates in percentage from 10/06/2006 to 05/12/2022 
    - SHIBOR is a daily reference rate that reflects the loan transactions between banks maturing from overnight to a year
    """
    )

# Page 3
if selected_page == "Macro Leverage Ratio":

    df = pd.read_csv('macro_leverage_ratio.csv')
    df = df.dropna()

    # df = px.data.stocks()
    fig = px.line(df, x="Date", y=df.columns,
                  hover_data={"Date": "|%B %d, %Y"},
                  title='Macro Leverage Ratio')

    fig
    st.markdown(
    """
    Macro Leverage Ratio (Debt/GDP) in percentage is a quarterly data that quantifies the economic stability of China from 03/01/2005 to 03/01/2022 
    - Higher ratios are signs of excessive liquidity in the market, making it vulnerable when the economy slows down expanding
    """
    )

# Page 4
if selected_page == "National Enterprise Index":

    df = pd.read_csv('national_enterprise_index.csv')
    df = df.dropna()

    # df = px.data.stocks()
    fig = px.line(df, x="Date", y=df.columns,
                  hover_data={"Date": "|%B %d, %Y"},
                  title='National Enterprise Index')

    fig
    st.markdown(
    """
    Quarterly data of National Enterprise Indices that represent the prospect of Chinese companies and 
    confidence of Chinese entrepreneurs from 03/01/2005 to 12/01/2021 
    """
    )

# Page 5
if selected_page == "Tax Income":

    df = pd.read_csv('tax_income.csv')
    df = df.dropna()

    # df = px.data.stocks()
    fig = px.line(df, x="Date", y=df.columns,
                  hover_data={"Date": "|%B %d, %Y"},
                  title='Tax Income')

    fig
    st.markdown(
    """
    Quarterly tax income data from 12/01/2009 to 03/01/2022
    """
    )
