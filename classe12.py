from dataclasses import dataclass
import os
os.system("cls || clear")


@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f"O Tittulo do livro é: {self.titulo}")
        print(f"O Ano é: {self.ano}")
        print(f"Livro produzido por: {self.autor.nome}")
        print(f"O nome do autor é: {self.autor.nome}")
        print(f"Biografia do autor: {self.autor.biografia}")

pessoa = Livro(titulo=input("Titulo do livro: "),
               ano=int(input("Ano do livro: ")),
               autor=Autor(
                   nome=input("Digite o nome do livro: "),
                   biografia=input("Digite sua biografia: ")))

print("\n Dados do autor.")
pessoa.exibir_detalhes()


