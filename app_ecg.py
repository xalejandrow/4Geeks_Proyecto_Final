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
    #st.text(result)
    test_result = result.tolist()[0]
    #st.text(test_result)
    return test_result

pred = None
if file is not None:
    df= pd.read_csv(file, header=None)
    st.dataframe(df)
    st.title('ECG Graph')
    st.line_chart(df.iloc[0,:186])
    #calcPrediction(df[0,0:186])
    pred = calcPrediction(df)
    #calcPrediction(df[:,-1])


tabla_switch = {
    0.0:'Normal',
    1.0:'Supraventricular',
    2.0:'Ventricular',
    3.0:'Fusion',
    4.0:'Unknown'
}

if pred is not None:
    st.header('Resultado del ECG:')
    st.subheader(tabla_switch[pred])
