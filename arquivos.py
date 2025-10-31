import os
os.system("cls || clear")

# Texto que desejo salvar
texto = input("Digite seu nome: ")

#Definir nome do do arquivo
nome_arquivo = "exemplo.txt"

# Comando para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n") 
    print("salvo com sucesso")