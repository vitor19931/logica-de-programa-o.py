import os
os.system("cls || clear")



data =int(input("Digite o mês: "))

match data:
    case 1:
        print("mês de janeiro")
    case 2:
        print("mês de fevereiro")
    case 3:
        print("Mês de março")
    case 4:
        print("Mês de abril")
    case 5:
        print("Mês de maio")
    case 6:
        print("Mês de junho")
    case 7:
        print("Mês de julho")
    case 8:
        print("Mês de agosto")
    case 9:
        print("Mês de setembro")
    case 10:
        print("Mês de outubro")
    case 11:
        print("Mês de novembro") 
    case 12:
        print("Mês de dezembro")                       
    case _:
        print("invalido")            
