import os
os.system("cls || clear")

def limpa_tela():
    os.system("cls || clear")

def mult(n1):
    return n1 * 100

def mostrar_resultado(multiplicacao):
    print(f"Resultado: {multiplicacao} cm")



limpa_tela()
numero = float(input("Digite um número para converter em cm: "))
resultado = mult(numero)
mostrar_resultado(resultado)