import os
os.system("cls || clear")

numero = int(input("Digite seu numero: ")) 

if numero <= 15:
    print("não podem votar")
elif numero <18:
    print("voto opcional") 
elif numero <= 65:
    print("voto obrigatorio")    

else:
     print("não é preciso mais votar")