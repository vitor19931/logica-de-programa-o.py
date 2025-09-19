import os
os.system("cls || clear")

soma = 0
quantidade = 0

while True:
    notas = float(input("Digite q nota do aluno: "))
    soma += notas
    quantidade += 1
    continuar = input("Deseja adicionar mais notas? (s/n): ").lower()
    if continuar != 's':
        break
media = soma / quantidade
print(f"Sua média é: {media:.2f}")
print(f"Foram inseridas {quantidade} notas.")
print(f"A soma total das notas é: {soma:.2f}")
print("Obrigado por usar o sistema de notas!")
