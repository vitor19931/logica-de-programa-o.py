import os
os.system("cls || clear")


def teste(numero):
    print(f"O número digitado foi {numero}")
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")


numero = int(input("Digite um número: "))
teste(numero)