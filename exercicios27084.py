import os
os.system ("cls || clear")

quantidade = int(input("informe a quantidade de maças: "))

if quantidade <= 12:
    preco_unitario = 1.30
else:
    preco_unitario = 1.00

valor_total = quantidade * preco_unitario


print(f"preço total: {valor_total}")
