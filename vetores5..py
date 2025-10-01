import os
os.system("cls || clear")

lista_notas = []

QUANTIDADES_NOTAS = 5

for i in range(QUANTIDADES_NOTAS):
    nota = int(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

maior_nota = max(lista_notas)
menor_nota = min(lista_notas)
    
for i in range(QUANTIDADES_NOTAS):
     print(f"\nNota: {lista_notas[i]}")
    
    
print(f"\n Maior nota: {maior_nota}")     
print(f"\n Menor nota: {menor_nota}")     
