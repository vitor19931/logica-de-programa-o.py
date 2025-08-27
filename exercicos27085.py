import os
os.system ("cls || clear")


nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))



media = (nota1 + nota2) /2

if media >= 9:
    conceito = "A"
    resultado = "aprovado"
elif media >= 7.5 < 9:
    conceito = "B"
    resultado = "aprovado"  
elif media >=6 <7.5:
    conceito = "C"
    resultado = "aprovado"
elif media >=4 <6:
    conceito = "D"
    resultado = "reprovado"

else:
    conceito = "E"
    resultado = "reprovado"
   
   
print(f"\nMédia {media}")
print(f"Conceito {conceito}")
print(f"Resultado {resultado}")