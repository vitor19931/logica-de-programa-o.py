import os
os.system("cls || clear")

primeiro_semestre = float(input("Nota do primeiro semestre :"))
segundo_semestre = float(input("Nota do segundo semestre :"))
terceiro_semestre = float(input("Nota do segundo semestre:"))

media = (primeiro_semestre + segundo_semestre + terceiro_semestre) /3


if media <7:
    print("o aluno foi: reprovado")
elif media >= 6 and media <= 6.9:
    print("rebolou pros crias")
elif media >7 :
    print("o aluno foi: aprovado")    