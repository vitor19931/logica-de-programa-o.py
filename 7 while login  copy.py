import streamlit as st

st.write("Escreva um algoritmo que solicite a senha e o login do usuário")

login_cadastrado = "Vitor1234"
senha_cadastrada = "27052006"


if "tentativas" not in st.session_state:
    st.session_state["tentativas"] = 0 


login_informado = st.text_input("Digite seu usuário: ")
senha_informada = st.text_input("Digite sua senha: ", type="password")
tentativas = 0  

if st.button("Verificar"):
        if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
            st.success("Bem-vindo!")
       
          
        else:
                st.session_state["tentativas"] += 1
                st.error("Usuario ou senha erradas, tente novamente")
        if st.session_state["tentativas"] >= 3:
              st.warning("numero de tentivas alcançado tente novamente mais tarde")        