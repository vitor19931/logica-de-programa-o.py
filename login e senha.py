import os
os.system("cls || clear")

login_cadastrado = "vitor1234"
senha_cadastrada = "27052006"

login_informado = input("INFORME O USUARIO: ")
senha_informada = input("INFORME A SENHA: ")

if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
    print("Usuario e senha correta")

else:
    print("INCORRETA")   