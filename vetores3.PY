import os
os.system("cls || clear")

lista_notas = []

QUANTIDADES_NOTAS = 3


for i in range(3):
    nota = int(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = sum(lista_notas) / QUANTIDADES_NOTAS

for i in range(QUANTIDADES_NOTAS):
    print(f"\nNota: {lista_notas[i]}")



print(f"\nSoma: {soma}")
print(f"\nMedia: {media}")
print("\nFIM")