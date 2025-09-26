import os
os.system("cls || clear")

pares = 0
impares = 0
soma_pares = 0
soma_impares = 0
contador_geral = 0
soma_geral = 0

while True:
    numero = int(input("Digite um numero: "))
    if numero > 0:
        contador_geral += 1
        soma_geral += numero
        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else: 
            impares += 1
    if numero == 0:
        break

media_pares = soma_pares / pares if pares != 0 else 0
media_geral = soma_geral / contador_geral if contador_geral != 0 else 0
 
  

print(f"\nquantidade de pares: {pares}")    
print(f"quantidade de impares: {impares}")    
print(f"Media de numeros pares: {media_pares}")    
print(f"Media geral: {media_geral}")    