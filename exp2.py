
import os
os.system ("cls || clear")


num1 = float(input("Digite o num1: "))
num2 = float(input("Digite o num2: "))
num3 = float(input("Digite o num3: "))

media = (num1 + num2 + num3) /3

if media <5:
    print("o aluno foi reprovado: ")
elif media >= 5 and media <= 5.9:
    print("rodou na boca da recuperação")
elif media >6:
    print("o aluno foi aprovado")    