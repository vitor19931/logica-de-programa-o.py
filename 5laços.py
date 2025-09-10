import streamlit as st

st.title("Media")

nota1 = st.number_input("Digite a sua primeira nota: ")
nota2 = st.number_input("Digite a sua segunda nota: ")


soma = nota1 + nota2
subtracao = nota1 - nota2
multiplicacao = nota1 * nota2
media = (nota1 + nota2) /2
menor = min(nota1, nota2)
maior = max(nota1, nota2)

if st.button("Verificar"):
    st.write(f"A soma das duas notas é: {soma}")
    st.write(f"A subtracao das duas notas é: {subtracao}")
    st.write(f"menor: {menor}")
    st.write(f"Maior: {maior}")
    st.write(f"A Media do aluno é: {media}")


else:
    st.info("informe os numeros")













# sucess - verde
# warning - amarelo
# info - azul
# error - vermelho

        