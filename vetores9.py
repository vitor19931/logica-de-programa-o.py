import os
os.system("cls || clear")

lista_de_numeros = []
QUANTIDADE_DE_NUMEROS = 5
negativos = 0

for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero < 0:
        numero = 0 
    lista_de_numeros.append(numero)
    os.system("cls")

print("\nexibindo numeros")
for i, numero in enumerate(lista_de_numeros):
    print(f"{i + 1}º número: {numero}")
print("lista de números:", lista_de_numeros)