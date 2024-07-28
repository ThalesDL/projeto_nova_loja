import streamlit as st
import pandas as pd
from datetime import date

def gravar(data, nome, genero, nascimento, telefone, endereco, cidade):
    if nome and data <= date.today() and nascimento <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{data};{nome};{genero};{nascimento};{telefone};{endereco};{cidade}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(page_title="CADASTRO NOME_LOJA", page_icon="🎁")
st.image("baner.png")
st.title("CADASTRO DE CLIENTES")
st.divider()

##inserindo a data de cadastro
data = st.date_input("Digite a data do cadastro: ",
                     key="input_data",
                     format="DD/MM/YYYY")
###st.text(data.strftime(format="%d/%m/%Y"))

#inserindo o nome de cadastro
nome = st.text_input("Digite o nome para cadastro: ", placeholder="digitar",
                     key="input_nome", max_chars=30)
###st.text(nome)

##inserindo o gênero
genero = st.radio("Escolha o gênero: ",
                 ["masculino", "feminino", "prefere não optar"])

#inserindo a data de aniversário
nascimento = st.date_input("Digite a data de nascimento: ",
                      key="input_niver", format="DD/MM/YYYY")
###st.text(aniversario.strftime(format="%d/%m/%Y"))

#inserindo o número de telefone
telefone = st.text_input("Digite o número de telefone (DD): ", placeholder="digitar",
                       key="input_tel", value=None, max_chars=13)
###st.text(telefone)

#inserindo o endereço
endereco = st.text_input("Digite o endereço: ", key="input_end", max_chars=30, placeholder="digitar")
###st.text(endereco)

#inserindo a cidade
cidade = st.selectbox("Escolha a cidade:",
                      ["Lorena", "Guaratinguetá", "Cruzeiro",
                       "Aparecida", "Taubaté", "Outra"])
st.divider()

#inserindo botão para concluir cadastro
botao = st.button("Clique aqui para cadastrar",
                  on_click=gravar,
                  args=[data, nome, genero, nascimento, telefone, endereco, cidade])

if botao:
    if st.session_state["sucesso"]:
        st.success("Cadastro concluido com sucesso!", icon="😁")
    else:
        st.error("Houve algum problema no cadastro", icon="😣")
