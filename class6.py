from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class dados_da_pessoa:
    nome: str
    endereco: str
    email: str

    def mostrar_dados(self):
        print("\n= Mostrar dados =")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")


    def mostrar_somente_nome(self):
        print("\n= mostrar_somente_nome =")
        print(f"Nome: {self.nome}")


print("\n Solicitando dados da pessoa.")
pessoa1 = dados_da_pessoa(nome=input("Digite seu nome: "),
                          endereco=input("Digite seu endereço: "),
                          email=input("Digite seu email: "))

print("\n Solicitando dados da pessoa.")
pessoa2 = dados_da_pessoa(nome=input("Digite seu nome: "),
                          endereco=input("Digite seu endereço: "),
                          email=input("Digite seu email: "))

print("\nExibindo dados")
pessoa1.mostrar_dados()
pessoa1.mostrar_somente_nome()
pessoa2.mostrar_dados()
pessoa2.mostrar_somente_nome()

              
