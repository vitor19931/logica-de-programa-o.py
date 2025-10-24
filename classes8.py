from dataclasses import dataclass
import os
os.system("cls || clear")


@dataclass
class endereco:
    lougradouro: str
    numero: int
    
@dataclass
class Pessoa:
    nome: str
    Endereco: endereco


pessoa1 = Pessoa(nome="Marta", 
                 Endereco=endereco(lougradouro="Rua A", numero=23))

print("Mostrar dados do cliente.")
print(f"Nome: {pessoa1.nome}")
print(f"Endereço: {pessoa1.Endereco.lougradouro}")
print(f"Numero: {pessoa1.Endereco.numero}")