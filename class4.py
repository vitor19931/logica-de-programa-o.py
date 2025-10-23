from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class pessoa:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

print("Solicitando os dados da pessoa.")
pessoa1 = pessoa(nome=input("Digite seu nome: "),
                 idade = int(input("Digite sua idade: ")))    
os.system("cls || clear")
pessoa2 = pessoa(nome=input("Digite seu nome: "),
                 idade = int(input("Digite sua idade: ")))    

print("\n= Exibindo dados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()

              
