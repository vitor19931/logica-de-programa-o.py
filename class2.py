from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass 
class dadospessoais:
    nome: str
    email: str
    telefone: int
    endereço: str

print("Exibindo dados da pessoa")
pessoa1 = dadospessoais(nome= input("Digite seu nome: "),
                        email=input("Digite seu email: "),
                        telefone=int(input("Digite seu telefone: ")),
                        endereço=input("Digite seu endereço: "))
                    
os.system("cls")
print("Exibindo dados: ")
print(f"Nome: {pessoa1.nome},\nEmail: {pessoa1.email},\nTelefone: {pessoa1.telefone},\nEndereço: {pessoa1.endereço}")