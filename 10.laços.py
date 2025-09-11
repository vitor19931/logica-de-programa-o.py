import streamlit as st
import time

st.title("Atividade")

st.header("Apresente a soma ")

st.write("Escrever um programa de computador que solicite do usario 5 " \
"numeros inteiros e, ao final apresente a soma de todos os numeros lidos.")

soma = 0



for i in range(1,6 ):
        numero = st.number_input(f"Digite o {i} numero: ", step=1, min_value=0)
        soma = soma + numero
        time.sleep(1)

if st.button("Iniciar"): 
      st.success(f"A soma dos numeros é: {soma}")       
       
   
else:
    st.info("Informe os numeros")    