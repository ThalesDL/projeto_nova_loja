import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="CADASTRO PRODUTO", page_icon="🛒")
st.image("imagem.png")
st.title("CADASTRO DE PRODUTOS")
st.divider()

#inserindo os produtos
lista = st.subheader("Anote os itens da compra")

col1, col2 = st.columns(2)

caneta = col1.checkbox("Caneta")
if caneta:
    nr_caneta = col1.number_input("Quantidade: ", placeholder="digitar", key="nr_caneta",
                                step=1, value=None)
else:
     nr_caneta = 0

lapis = col1.checkbox("Lápis")
if lapis:
    nr_lapis = col1.number_input("Quantidade: ", placeholder="digitar", key="nr_lapis",
                                step=1, value=None)
else:
     nr_lapis = 0

borracha = col1.checkbox("Borracha")
if borracha:
    nr_borracha = col1.number_input("Quantidade: ", placeholder="digitar", key="nr_borracha",
                                step=1, value=None)
else:
     nr_borracha = 0

caderno = col1.checkbox("Caderno")
if caderno:
    nr_caderno = col1.number_input("Quantidade: ", placeholder="digitar", key="nr_caderno",
                                step=1, value=None)
else:
     nr_caderno = 0

regua = col1.checkbox("Régua")
if regua:
    nr_regua = col1.number_input("Quantidade: ", placeholder="digitar", key="nr_regua",
                                step=1, value=None)
else:
     nr_regua = 0

cola = col2.checkbox("Cola")
if cola:
    nr_cola = col2.number_input("Quantidade: ", placeholder="digitar", key="nr_cola",
                                step=1, value=None)
else:
     nr_cola = 0

apontador = col2.checkbox("Apontador")
if apontador:
    nr_apontador = col2.number_input("Quantidade: ", placeholder="digitar", key="nr_apontador",
                                step=1, value=None)
else:
     nr_apontador = 0

compasso = col2.checkbox("Compasso")
if compasso:
    nr_compasso = col2.number_input("Quantidade: ", placeholder="digitar", key="nr_compasso",
                                step=1, value=None)
else:
     nr_compasso = 0

giz = col2.checkbox("Giz")
if giz:
    nr_giz = col2.number_input("Quantidade: ", placeholder="digitar", key="nr_giz",
                                step=1, value=None)
else:
     nr_giz = 0

estojo = col2.checkbox("Estojo")
if estojo:
    nr_estojo = col2.number_input("Quantidade: ", placeholder="digitar", key="nr_estojo",
                                step=1, value=None)
else:
     nr_estojo = 0

botao2 = st.button("Clique aqui para cadastrar", key="clk_botao2")

if botao2:
    with open("produtos.csv", "a", encoding="utf-8") as file:
            file.write(f"{nr_caneta},{nr_lapis},{nr_borracha},{nr_caderno},{nr_regua},{nr_cola},{nr_apontador},{nr_compasso},{nr_giz},{nr_estojo}\n")
            st.success("Cadastro concluido com sucesso!", icon="😁")
     