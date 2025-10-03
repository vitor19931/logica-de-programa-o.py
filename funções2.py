import os
os.system("cls || clear")

# criando uma função
def saudacao(nome, idade, peso, altura):
    print(f"Olá, {nome} seja bem vindo(a)")
    print(f"Sua idade é {idade} anos")
    print(f"Seu peso é {peso} kg")
    print(f"Sua altura é {altura} m") 
# chamando a função 

def limpeza():
     os.system("cls")

limpeza()     
nome = input("Digite seu nome: ")
limpeza()     
idade = int(input("Digite sua idade: "))
limpeza()     
peso = float(input("Digite seu peso: " ))
limpeza()     
altura = float(input("Digite sua altura: " ))
limpeza()     
saudacao(nome, idade, peso, altura)


