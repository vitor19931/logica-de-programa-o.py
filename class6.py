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
        print("\n= somente nomes =")
        print(f"Nome: {self.nome}")


print("\n Solicitando dados da pessoa.")
lista_pessoas = []

for i in range(2):
    pessoa = dados_da_pessoa(nome=input("Digite seu nome: "),
                          endereco=input("Digite seu endereço: "),
                          email=input("Digite seu email: "))
    lista_pessoas.append(pessoa)

print("\nExibindo dados")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()
print("\n= Somente nomes =")
for pessoa in lista_pessoas:
    pessoa.mostrar_somente_nome()

              
