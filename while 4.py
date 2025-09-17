import streamlit as st

st.title("Laços de repetição")

st.write("Escreva um algoritimo que solicite duas notas para um aluno" \
"Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente" \
"calcule e mostre a media aritmetica do aluno.")

nota1 = st.number_input("Digite a primeira nota: ", min_value=0, max_value=10)
nota2 = st.number_input("Digite a segunda nota: ", min_value=0, max_value=10)

media = (nota1 + nota2) / 2

if st.button("Calcular"):
    st.info(f"Media: {media}")