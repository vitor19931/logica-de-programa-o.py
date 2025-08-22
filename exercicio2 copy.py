import os
os.system ("cls || clear")

numero1 = int(input("nota numero1: "))
numero2 = int(input("nota numero2: "))

soma = numero1+numero2
media = (numero1+numero2)/2
produto = numero1*numero2

if numero1 < numero2:
    print("Segundo numero é maior que numero1")
else :
    print("primeiro numero é maior que numero2")   
    
print(f"soma:{soma}\nmedia:{media}\nproduto:{produto}")