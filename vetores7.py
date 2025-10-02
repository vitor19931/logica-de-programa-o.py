import os
os.system("cls || clear")

import os
os.system("cls || clear")

lista_de_pratos = []
QUANTIDADE_DE_PRATOS = 8

print("========Cardapio=======")
print("1 - Picanha.........25.00")
print("2 - Lasanha.........20.00")
print("3 - Strogonoff.........18.00")
print("4 - Bife acebolado.........15.00")
print("5 - Pão com ovo.........5.00")

print("==========Sobremesas==========")
print("6 - Pudim.........12.00")
print("7 - Casquinha.......6.00")
print("8 - Bolo de pote 10.00")

menu = int(input("Digite o código do prato desejado: "))

for i in range(QUANTIDADE_DE_PRATOS):
    prato = int(input(f"Digite o {i + 1}º código do prato desejado: "))
    

soma = 0
for prato in lista_de_pratos:
    match prato:
        case 1:
            soma += 25.00
        case 2:
            soma += 20.00
        case 3:
            soma += 18.00
        case 4:
            soma += 15.00
        case 5:
            soma += 5.00
        case 6:
            soma += 12.00
        case 7:
            soma += 6.00
        case 8:
            soma += 10.00
        case _:
            print("Prato inválido")
    while True:
        resposta = input("Deseja pedir mais algum prato? (s/n): ").lower()
        if resposta in ['s', 'n']:
            break
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
    if resposta == 'n':
        break

print(f"Total a pagar: R$ {soma:.2f}")
lista_de_pratos.append(prato)
print("Mostrando os pratos pedidos: ")
for prato in lista_de_pratos:
    print(f"Prato: {prato}")