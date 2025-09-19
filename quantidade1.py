import os
os.system("cls || clear")

# faça um alooritmo que leia uma quantidade não determinada de numeros inteiros positivos, calcule 

soma = 0
quantidade = 0
pares = 0
impares = 0
while True:
    numero = int(input("Digite um número (ou um número negativo para sair): "))
    if numero == 0:
        break
    soma += numero
    quantidade += 1 
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
if quantidade > 0:
    media = soma / quantidade
    print(f"A quantidade de números inseridos é: {quantidade}")
    print(f"A soma dos números inseridos é: {soma}")
    print(f"A média dos números inseridos é: {media:.2f}")
    print(f"A quantidade de números pares é: {pares}")
    print(f"A quantidade de números ímpares é: {impares}")
else:
    print("Nenhum número positivo foi inserido.")
print("Obrigado por usar o sistema de números!")