import streamlit as st
import time

st.title("Media escolar")

st.header("Apresente a media ")

st.write("Escrever um programa de computador que solicite a media do usario " \
" Ao final apresente a media de todos os numeros lidos.")

soma = 0
media = 0



for i in range(1,5 ):
        numero = st.number_input(f"Digite o {i} numero: ", step=1, min_value=0)
        soma = soma + numero
        media = soma / 4
        time.sleep(1)
        st.balloons()
    

if st.button("Iniciar"): 
      st.success(f"A media do usario é: {media}")       
       