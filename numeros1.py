import os
os.system("cls || clear")

# Programa que lê números até que um número negativo seja inserido / e ao final mosrre a media aritmética dos números positivos inseridos

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        print("Número negativo, encerrando o programa.")
        break 
    soma += numero
    quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print(f"A quantidade de números positivos inseridos é: {quantidade}")
    print(f"A média aritmética dos números positivos é: {media:.2f}")
    
else:
    print("Nenhum número positivo foi inserido.")
print("Obrigado por usar o sistema de números!")
