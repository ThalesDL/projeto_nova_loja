import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Listagem de Produtos", page_icon="📙")

st.title("PRODUTOS CADASTRADOS")
st.divider()

dados2 = pd.read_csv("produtos.csv")
#dados2.set_index("nr_caneta" , inplace=True)
st.dataframe(dados2)

tt_caneta = dados2["nr_caneta"].sum()
tt_lapis = dados2["nr_lapis"].sum()
tt_borracha = dados2["nr_borracha"].sum()
tt_caderno = dados2["nr_caderno"].sum()
tt_regua = dados2["nr_regua"].sum()
tt_cola = dados2["nr_cola"].sum()
tt_apontador = dados2["nr_apontador"].sum()
tt_compasso = dados2["nr_compasso"].sum()
tt_giz = dados2["nr_giz"].sum()
tt_estojo = dados2["nr_estojo"].sum()
dict = {"nr_caneta": tt_caneta, "nr_lapis": tt_lapis, "nr_borracha": tt_borracha,
        "nr_caderno": tt_caderno, "nr_regua": tt_regua, "nr_cola": tt_cola,
        "nr_apontador": tt_apontador, "nr_compasso": tt_compasso, "nr_giz": tt_giz,
        "nr_estojo": tt_estojo}
st.dataframe(dict)
