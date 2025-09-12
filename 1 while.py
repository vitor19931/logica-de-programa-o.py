import os 
os.system("cls || clear")

print("Laço de repetição - While")


while True:
    nota = int(input("Digite uma nota: "))
    if 0 <= nota <= 10:
        break
    print("Nota invalida! Digite novamente")

print(f"Nota informada: {nota}")



print("Fim")
