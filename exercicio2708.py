import os
os.system ("cls || clear")

num1 = int (input("Digite o num1: "))
num2 = int (input("Digite o num2: "))

soma = num1 + num2
media = (num1 + num2)/2
produto = num1*num2



if num1 < num2:
    print("menor valor")
else :
    print("maior valor") 

if num1 == num2:
    print("são numeros iguais")

 
 
print(f"soma:{soma}\nmedia:{media}\nproduto:{produto}")   
