import streamlit as st


st.write("Escreva um algoritimo que solicite a senha e o login do usuario")


login_cadastrado = "Vitor1234"
senha_cadastrada = "27052006"

login_informado = st.text_input("Digite seu usuario: ")
senha_informada = st.text_input("Digite sua senha: ", type="password")

if st.button("Verificar"):
    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        st.success("Bem vindo!")
    else:
        st.warning("Usuario e senha incorretas")    