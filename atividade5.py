import os
os.system("cls || clear")

altura = float(input("Digite sua altura em metros (exemplo: 1.86): "))
sexo = input("Digite seu sexo (M para Masculino, F para Feminino): ")

match sexo:
    case "M":
        peso_ideal = (72.7 * altura)-58
        print(f"seu peso ideal é: {peso_ideal:} kg")
    case "F":
        peso_ideal = (62.1 * altura)-44.7
        print(f"seu peso ideal é: {peso_ideal:} kg")
    case _:
        print("opção de sexo invalida")        