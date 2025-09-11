import streamlit as st
import time

st.title("Numeros")

st.header("Regressão")

numero = st.number_input("Digite o numero:  ", step = 1)


if st.button("Iniciar"):
    for i in range(numero, 0, -1 ):
        st.warning(i)
        time.sleep(1)
        st.snow()
   
else:
    st.info("Informe um numero")    