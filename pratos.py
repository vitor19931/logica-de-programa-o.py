import os
os.system("cls || clear")

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


menu = int(input("Digite o numero do pedido: "))
soma = 0
 
match menu:
    case 1:
        print("Picanha.........25.00")
        soma += 25.00
    case 2:
        print("Lasanha.........20.00")
        soma += 20.00
    case 3:
        print("Strogonoff.........18.00")
        soma += 18.00
    case 4:
        print("Bife acebolado.........15.00")
        soma += 15.00
    case 5:
        print("Pão com ovo.........5.00")
        soma += 5.00
    case 6:
        print("Pudim.........12.00")
        soma += 12.00
    case 7:
        print("Casquinha.......6.00")
        soma += 6.00
    case 8:
        print("Bolo de pote 10.00")
        soma += 10.00
    case _:
        print("Opção inválida")
while True:
    mais = input("Deseja pedir mais algo? (s/n): ").lower()
    if mais == 's':
        menu = int(input("Digite o numero do pedido: "))
        match menu:
            case 1:
                print("Picanha.........25.00")
                soma += 25.00
            case 2:
                print("Lasanha.........20.00")
                soma += 20.00
            case 3:
                print("Strogonoff.........18.00")
                soma += 18.00
            case 4:
                print("Bife acebolado.........15.00")
                soma += 15.00
            case 5:
                print("Pão com ovo.........5.00")
                soma += 5.00
            case 6:
                print("Pudim.........12.00")
                soma += 12.00
            case 7:
                print("Casquinha.......6.00")
                soma += 6.00
            case 8:
                print("Bolo de pote 10.00")
                soma += 10.00
            case _:
                print("Opção inválida")
    elif mais == 'n':
        break

else:
    print("Opção inválida, digite 's' ou 'n'.")        
       

print(f"Total a pagar: {soma:.2f}")