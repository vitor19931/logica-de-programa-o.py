import os
os.system("cls || clear")

lista_de_numeros = []
QUANTIDADE_DE_NUMEROS = 6
pares = 0
impares = 0

for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    lista_de_numeros.append(numero)    

print("Mostrando os números digitados e se são pares ou ímpares: ")
 
for numero in lista_de_numeros:
    print(f"Numero: {numero}") 



print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

