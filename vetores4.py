import os
os.system("cls || clear")

lista_notas = []

QUANTIDADES_NOTAS = 4

for i in range(QUANTIDADES_NOTAS):
    nota = int(input(f"Digite a {i+1}º nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / QUANTIDADES_NOTAS
    
for i in range(QUANTIDADES_NOTAS):
     print(f"\nNota: {lista_notas[i]}")

     
print("\n------Resultados------")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("recuperação")
else:
    print("Reprovado")     
print(f"Media: {media}")