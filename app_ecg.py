#importing required libraries

import streamlit as st
import pandas as pd
from io import StringIO 

#adding a file uploader

file = st.file_uploader("Please choose a file")

if file is not None:
    df= pd.read_csv(file, header=None)
    st.dataframe(df)
    st.title('ECG Graph')
    st.line_chart(df.iloc[0,:186])
