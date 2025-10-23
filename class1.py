from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass 
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("Exibindo dados da pessoa: ")
pessoa1 = pessoa(nome=input("Digite seu nome: "),
                 idade=int (input("Digite sua idade (anos): ")),
                 peso=float(input("Digite seu peso (kg): ")),
                 altura = float(input("Digite sua altura (m): ")))


print("exibindo dados da pessoa: ")
os.system("cls || clear")
print(f"Nome: {pessoa1.nome}\n Idade: {pessoa1.idade}\n Peso: {pessoa1.peso}\n Altura: {pessoa1.altura}")