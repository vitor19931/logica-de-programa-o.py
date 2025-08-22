import os
os.system("cls || clear")

nota1 = float(input("Digite a nota1:"))
nota2 = float(input("Digite a nota2:"))
nota3 = float(input("Digite a nota3:"))
nota4 = float(input("Digite a nota4:"))

media = (nota1 + nota2 + nota3 + nota4) /4


if media <6:
    print("o aluno foi: reprovado")
elif media >= 6 and media <= 6.9:
    print("foi para recuperação")
elif media >7 :
    print("o aluno foi: aprovado")    