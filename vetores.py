import os
os.system("cls || clear")

soma = 0


for i in range(3):
    nota = int(input(f"Digite a {i+1}º nota: "))
    soma += nota


print(f"Nota: {nota}")
print(f"Soma: {soma}")
print("FIM")    