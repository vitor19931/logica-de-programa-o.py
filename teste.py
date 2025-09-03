import os
os.system("cls || clear")

print("========Cardapio=======")
print("1 - Picanha.........25.00")
print("2 - Lasanha.........20.00")
print("3 - Strogonoff.........18.00")
print("4 - Bife acebolado.........15.00")
print("5 - Pão com ovo.........5.00")





menu = int(input("Digite o numero do pedido: "))

match menu:
    case 1:
        print("Você escolheu o prato - Picanha - 25.00")
    case 2:
        print("Você escolheu o prato - Lasanha - 20.00 ")
    case 3:
        print("Você escolheu o prato - Strogonoff - 18.00") 
    case 4:
        print("Você escolheu o prato - Bife acebolado - 15.00")
    case 5:
        print("Você escolheu o prato - Pão com ovo - 5.00")              