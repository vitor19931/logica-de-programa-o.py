import os
os.system("cls || clear")

def inteiro(valor):
    for i in range(1, 10):
        print(f"{i} x {valor} = {i * valor}")

numero = int(input("Digite um número: "))
os.system("cls")
inteiro(numero)        
    