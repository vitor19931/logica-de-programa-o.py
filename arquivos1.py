from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        email=input("Digite seu email: "),
        telefone=int(input("Digite seu telefone: "))
    )
    os.system("cls || clear")
    lista_alunos.append(aluno)

print()
print("Salvando dados")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivos_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n")
    print("Salvo com sucesso")    