from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class dados_da_pessoa:
    nome: str
    endereco: str
    email: str

    def dados_entrega(self):
        print("\n= Dados de entrega =")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print("\n= Dados de e-mail marketing =")
        print(f"Nome: {self.nome}")
        print(f"Email; {self.email}")

print("\n Solicitando dados da pessoa.")
pessoa1 = dados_da_pessoa(nome=input("Digite seu nome: "),
                          endereco=input("Digite seu endereço: "),
                          email=input("Digite seu email: "))

print("\nExibindo dados")
pessoa1.dados_entrega()
pessoa1.dados_email_marketing()

              
