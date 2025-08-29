import os
os.system("cls || clear")

login_cadastrado = "vlade1234"
senha_cadastrada = "vlade princesa da favela"

login_informado = (input("INFOME O LOGIN: "))
senha_informada = (input("INFORME A SENHA: "))

if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
    print("BEM VINDO VLADE!")
else:
    print("SENHA OU LOGIN INVALIDOS.")   