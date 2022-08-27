#importing required libraries

import streamlit as st
import pandas as pd
from io import StringIO 
import pickle

#adding a file uploader

file = st.file_uploader("Please choose a file")

def calcPrediction(data):
    #model = pickle.load('model.pkl')
    model = pickle.load(open('model.pkl','rb'))
    df = data.iloc[:,:-1]
    result = model.predict(df)
    st.text(result)
    test_result = result.tolist()[0]
    st.text(test_result)

if file is not None:
    df= pd.read_csv(file, header=None)
    st.dataframe(df)
    st.title('ECG Graph')
    st.line_chart(df.iloc[0,:186])
    #calcPrediction(df[0,0:186])
    calcPrediction(df)
    #calcPrediction(df[:,-1])