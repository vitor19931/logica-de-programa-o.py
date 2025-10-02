import os
os.system("cls || clear")

lista_de_numeros = []
QUANTIDADE_NUMEROS = 5
positivo = 0
negativo = 0
soma_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_de_numeros.append(numero)
    if numero > 0:
        positivo += 1
        soma_positivos += numero
    elif numero < 0:
        negativo += 1

print(f"\nQuantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Soma dos números positivos: {soma_positivos}")