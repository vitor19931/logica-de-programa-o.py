import os
os.system("cls || clear")

def inteiro(valor):
    if valor > 0:
        print("O número é positivo")
    else:
        print("O número é negativo")     


numero = int(input("Digite um número: "))
os.system("cls")
inteiro(numero)        