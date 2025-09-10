# Verifique a idade de uma pessoa
# Se menor que 18, mostre: menor de idade 
# caso contrario, mostre: Maior de idade 
# usando streamlit

import streamlit as st

st.title("Verificação de idade")

idade = st.number_input("Digite sua idade: ")

if st.button("Verificar"):
    if idade < 18:
        st.write("Menor de idade")
    else:
        st.write("maior de idade") 

else:
    st.warning("Por favor, digite a sua idade: ")           