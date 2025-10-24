from dataclasses import dataclass
import os
os.system("cls || clear")


@dataclass
class dados_da_pessoa:
    nome: str
    cpf: str
    telefone: str


    def mostrar_dados(self):
        print("\n= Mostrar dados =")
        print(f"Nome: {self.nome}")
        print(f"Cpf: {self.cpf}")
        print(f"Telefone: {self.telefone}")


    def dados_sms_marketing(self):
        print("\n= somente telefones =")
        print(f"Telefone: {self.telefone}")


print("\n Solicitando dados da pessoa.")
lista_pessoas = []

for i in range(3):
    pessoa = dados_da_pessoa(nome=input("Digite seu nome: "),
                             cpf=input("Digite seu cpf: "),
                             telefone=input("Digite seu telefone: "))
    os.system("cls || clear")
    
    lista_pessoas.append(pessoa)


print("\n= Exibindo dados =")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

print("\n Somente telefone")
for pessoa in lista_pessoas:
    pessoa.dados_sms_marketing()

