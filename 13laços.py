import streamlit as st
import time

st.title("Media escolar")

st.header("Apresente a media ")

st.write("Escrever um programa de computador que solicite a media do usario " \
" Ao final apresente a media de todos os numeros lidos.")

QUANTIDADE_NOTAS = 3    
soma = 0




for i in range(3):
        numero = st.number_input(f"Digite o {i+1}ªnota: ")
        soma = soma + numero
        media = soma / QUANTIDADE_NOTAS
        time.sleep(1)
        st.balloons()



    

if st.button("Iniciar"): 
      st.info(f"A media do usario é: {media}")
if media >=7:
       st.success("Aprovado")
elif media >= 4:
       st.warning("Recuperação") 
else:
       st.error("Reprovado")                   