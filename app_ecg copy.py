#importing required libraries
import os
import streamlit as st
import pandas as pd
from io import StringIO 
import pickle

#adding a file uploader

# Upload Model
#file_model = st.file_uploader("Please choose a Model file if not uploaded yet")
# check if the file has been uploaded
#if file_model:
    # strip the leading path from the file name
    #fn = os.path.basename(file_model)
     
   # open read and write the file into the server
   # open(fn, 'wb').write(fileitem.file.read())

# Upload CSV
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
