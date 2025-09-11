import streamlit as st
import time

st.title("Tabuada")

st.header("MUlTIPLICAÇÃ")

numero = st.number_input("Digite o numero para multiplicação:  ", step = 1)


if st.button("Iniciar"):
    for i in range(1,11 ):
        mult = numero * i
        st.write(f"{numero} * {i} = {mult}")
        time.sleep(1)
    st.success("FIM")