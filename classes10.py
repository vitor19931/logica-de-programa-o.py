from dataclasses import dataclass
import os
os.system("cls || clear")


import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")

lista_dados = []

for i in range(4):
     Pessoa(nome=input("Digite seu nome: "),
                 idade=int(input("Digite sua idade: (anos)")),
                 peso=float(input("Digite seu peso: (kg)")),
                 altura=float(input("DIgite sua altura: (m)")))
lista_dados.append(Pessoa)


print("\nMostrar dados do cliente.")
for pessoa in lista_dados:
    Pessoa.mostrar_dados()