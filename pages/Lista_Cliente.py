import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Listagem de Clientes", page_icon="📄")

st.title("CLIENTES CADASTRADOS")
st.divider()

dados = pd.read_csv("clientes.csv", sep=";")
#st.dataframe(dados)

dados["data"] = pd.to_datetime(dados["data"])
dados["data"] = dados["data"].dt.strftime("%d/%m/%Y")

dados["nascimento"] = pd.to_datetime(dados["nascimento"])
dados["nascimento"] = dados["nascimento"].dt.strftime("%d/%m/%Y")

dados.set_index("data", inplace=True)
st.dataframe(dados)


mostrar = st.toggle("Gráfico Cidades")
if mostrar:
    cidade = dados["cidade"].value_counts()
    st.bar_chart(cidade, color=(49, 131, 228), horizontal=True,
                 height=200)


st.write("Gêneros")
genero = dados["genero"].value_counts()
genero
#genero.plot(kind='pie')
