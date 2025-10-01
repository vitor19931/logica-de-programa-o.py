import os
os.system("cls || clear")

lista_notas = []


for i in range(3):
    nota = int(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
for i in range(3):
    print(f"Nota: {lista_notas[i]}")



print(f"Soma: {soma}")
print("FIM")