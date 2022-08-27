#importing required libraries

import streamlit as st
import pandas as pd
from io import StringIO 
import pickle

#adding a file uploader

file = st.file_uploader("Please choose a file")

def calcPrediction(df):
    #model = pickle.load('model.pkl')
    model = pickle.load(open('model.pkl','rb'))
    result = model.predict(df)
    test_result = result.tolist()[0]
    print(test_result)

if file is not None:
    df= pd.read_csv(file, header=None)
    st.dataframe(df)
    st.title('ECG Graph')
    st.line_chart(df.iloc[0,:186])
    calcPrediction(df[0,0:186])
    #calcPrediction(df[:,-1])