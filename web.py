import pandas  as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Establecimientos de Salud",layout="wide")
st.title("Establecimientos de Salud por Region")
st.markdown('''
Esta web muestra los establecimientos de salud con filtros segun tipo de atencion ''')



dataset_url = "https://datos.gob.cl/dataset/3bf4cf7c-f638-4735-9a01-f65faae4beca/resource/2c44d782-3365-44e3-aefb-2c8b8363a1bc/download/establecimientos_20251223.csv"

@st.cache_data 
def load_data(url):
    df = pd.read_csv(url, sep=";", encoding="latin-1")
    return df

df = load_data(dataset_url)


st.subheader ("Establecimientos de salud ")
st.write(df)

st.write("columnas del dataset: ",df.columns.tolist())

st.sidebar.header ("filtros")

Region = df ["RegionGlosa"].unique()
Sistema = df ["TipoSistemaSaludGlosa"].unique()

region_seleccionada = st.sidebar.selectbox ("seleccione una region",Region)
sistema_seleccionado = st.sidebar.selectbox ("seleccione un sistema",Sistema)

