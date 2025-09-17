import streamlit as st

st.title("Laco de repeticao: While")
st.write("Crie um programa que solicite ao usuario seu login e uma senha. 0 programa deve continua")

login_salvo = "marta"
senha_salva = "123"

st.session_state.setdefault("campo", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("Digite seu login: ", disabled=st.session_state.campo)
senha = st.text_input("Digite sua senha: ", type="password", disabled=st.session_state.campo)


if st.button("Verificar"):
    if login == login_salvo and senha == senha_salva:
        st. success("Bem-vindo!")
else:
    st.session_state.tentativas += 1
    if st.session_state.tentativas <= 3:
        st.warning(f"login ou senha invalidos,  tentativas: {st.session_state.tentativas}")
    else:
        st.session_state.desabilitar = True
        st.error("Numero de tentativas invalida")    