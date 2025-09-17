import os
os.system("cls || clear")

login_cadastrado = "vitor1234"
senha_cadastrada = "27052006"


while True:
    login_informado = input("Informe seu login: ")
    senha_informada = input("Informe sua senha: ")


    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
     print("usuario e senha corretas")

    else:
        print("usuario e senha incorretas")


