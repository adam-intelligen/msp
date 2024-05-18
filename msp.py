import streamlit as st
import pandas as pd
import numpy as np

st.title('MSP Data')

DATA_URL = ('https://am-bucket-123.s3.ap-southeast-2.amazonaws.com/' 
         'test/MSP.csv')

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


st.map(data, size='percentage')
