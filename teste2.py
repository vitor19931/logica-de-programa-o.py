import os
os.system("cls || clear")

print("===============BOLETIM==============")

primeiro_semestre = float(input("Digite a nota do primeiro_semestre: "))
segundo__semestre = float(input("Digite a nota do segundo_semestre: "))
terceiro__semestre = float(input("Digite a nota do terceiro_semestre: "))
quarto_semestre = float(input("Digite a nota do quarto_semestre: "))


soma = primeiro_semestre + segundo__semestre + terceiro__semestre + quarto_semestre /4
media = (primeiro_semestre + segundo__semestre + terceiro__semestre + quarto_semestre) /4


if media <=5.9:
    print("O aluno foi reprovado")
else:
    print("O aluno foi aprovado") 