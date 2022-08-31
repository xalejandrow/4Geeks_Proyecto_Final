#importing required libraries
import streamlit as st
import pandas as pd
from io import StringIO 
import pickle


st.title('Proyecto Final Machine Learning')

st.header('Descripción del ECG')
#st.image('img/PQRST-1.jpg')
#st.caption('fuente: https://www.girodmedical.es/blog_es/como-interpretar-un-electrocardiograma/')
st.image('img/UTII-2B-img-Elementos-del-electro.jpg')
st.caption('fuente: https://fisiologia.facmed.unam.mx/index.php/taller-de-interpretacion-del-electrocardiograma/')
#adding a file uploader

st.header('Clases detectadas')
st.image('img/Graficas_de_Clases.png')

#imprimo tabla de clases
#df_clases['Clase'] = {0,1,2,3,4}
clases = {'Clase':[0,1,2,3,4],'Name':['Normal','Supraventricular','Ventricular','Fusion','Unknown']}
df_clases = pd.DataFrame(clases)
df_clases.reset_index()
#df_clases = []
st.table(df_clases)

# Upload CSV
file = st.file_uploader("Seleccione un archivo para procesar")

def calcPrediction(data):
    model = pickle.load(open('model.pkl','rb'))
    df = data.iloc[:,:-1]
    result = model.predict(df)
    test_result = result.tolist()[0]
    return test_result

pred = None
if file is not None:
    df= pd.read_csv(file, header=None)
    st.dataframe(df)
    st.title('ECG Graph')
    st.line_chart(df.iloc[0,:186])
    pred = calcPrediction(df)


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
