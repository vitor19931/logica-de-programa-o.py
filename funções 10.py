import os
os.system("cls || clear")


def limpa_tela():
    os.system("cls || clear")


def produto(preco):
    if preco >=100:
        return preco * 1.2
    else:
        return preco * 1.1

def mostrar_resultado(preco):
    print(f"Resultado: {preco}")


limpa_tela()
preco = float(input("Digite o preço do produto: R$ "))
mostrar_resultado(produto(preco))

