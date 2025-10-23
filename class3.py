from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass 
class dadospessoais:
    nome: str
    email: str
    telefone: int
    endereço: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome},\nEmail: {self.email},\nTelefone: {self.telefone},\nEndereço: {self.endereço}")

print("Exibindo dados da pessoa")
pessoa1 = dadospessoais(nome= input("Digite seu nome: "),
                        email=input("Digite seu email: "),
                        telefone=int(input("Digite seu telefone: ")),
                        endereço=input("Digite seu endereço: "))
                    
os.system("cls")
print("Exibindo dados: ")
pessoa1.mostrar_dados()