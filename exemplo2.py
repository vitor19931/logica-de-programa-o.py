import os
os.system("cls || clear")

print("""
Codigo \t\t Prato \t\t\t Valor
      \t
   1 \t\t Picanha \t\t R$ 25.00
      \t
   2 \t\t Lasanha \t\t R$ 20.00
      \t
   3 \t\t Strogonoff \t\t R$ 18.00
      \t
   4 \t\t Bife acebolado \t R$ 15.00
      \t
   5 \t\t Pão com ovo \t\t R$ 5.00               
""")

codigo = int(input("Digite o codigo do prato desejado: "))


match codigo:
    case "1":
        print("Você escolheu o prato Picanha - 25.00")
    case "2":
        print("Você escolheu o prato Lasanha - 20.00")
    case "3":
        print("Você escolheu o prato Strogonoff - 18.00")
    case "4":
        print("Você escolheu o prato Bife acebolado - 15.00")
    case "5":
        print("Você escolheu o prato Pão com ovo - 5.00")
    case _:
        print("invalido")            