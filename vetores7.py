import os
os.system("cls || clear")

lista_de_pratos = []

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

Resposta = "s"

while Resposta == "s":
    prato = int(input("Digite o código do prato desejado: "))

    if prato >=1 and prato <=8:
        lista_de_pratos.append(prato)
        Resposta = input("Deseja adicionar mais algum prato? (s/n) ").lower()
    else:
        print("Código inválido. Tente novamente.")

soma = 0
print("\n=======Pratos pedidos=======")
for prato in lista_de_pratos:
    if prato == 1:
        print("Picanha - R$25.00")
        soma += 25.00
    elif prato == 2:
        print("Lasanha - R$20.00")
        soma += 20.00
    elif prato == 3:
        print("Strogonoff - R$18.00")
        soma += 18.00
    elif prato == 4:
        print("Bife acebolado - R$15.00")
        soma += 15.00
    elif prato == 5:
        print("Pão com ovo - R$5.00")
        soma += 5.00
    elif prato == 6:
        print("Pudim - R$12.00")
        soma += 12.00
    elif prato == 7:
        print("Casquinha - R$6.00")
        soma += 6.00
    elif prato == 8:
        print("Bolo de pote - R$10.00")
        soma += 10.00        

print(f"\nTotal a pagar: R${soma:.2f}")
print("Obrigado pela preferência! Volte sempre!")