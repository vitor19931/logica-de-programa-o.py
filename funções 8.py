import os
import time
os.system("cls || clear")

def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls || clear")


def somar(n1, n2):
    return n1 + n2 

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2 if n2 != 0 else "Divisão por zero"

def maior_resultado(soma, subtracao, multiplicacao, divisao):
    print(f"Resultado da soma: {soma}")
    print(f"Resultado da subtração: {subtracao}")
    print(f"Resultado da multiplicação: {multiplicacao}")
    print(f"Resultado da divisão: {divisao}")


limpa_tela()
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite outro número: "))

soma = somar(primeiro_numero, segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
multiplicacao = multiplicar(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)
maior_resultado(soma, subtracao, multiplicacao, divisao)
