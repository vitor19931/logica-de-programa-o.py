from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float

QUANTIDADE_LIVROS = 3
lista_livros = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        nome=input("Digite o nome do livro: "),
        autor=input("Nome do autor: "),
        categoria=input("Digite a categoria do livro: "),
        preço=float(input("Digite o preço do livro: ")),
        )
    
    os.system("cls || clear")
    lista_livros.append(livro)

print()
print("Salvando dados")
arquivo = "catalogo_de_livros.txt"

with open(arquivo, "a") as arquivos_livros:
    for livro in lista_livros:
        arquivos_livros.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preço}\n")
    print("Salvo com sucesso")    