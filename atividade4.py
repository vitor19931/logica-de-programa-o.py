import os
os.system("cls || clear")

valor_produto = float(input("Informe o valor do produto: R$ "))
print("Formas de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento à prazo")
forma_pagamento = int(input("Escolha a forma de pagamento (1 ou 2): "))

match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print("\nPagamento à vista:")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
    
    case 2:
        parcelas = int(input("Informe a quantidade de parcelas (até 6): "))
        if parcelas > 6:
            print("Número de parcelas inválido, máximo 6.")
        else:
            valor_parcela = valor_produto / parcelas
            print("\nPagamento à prazo:")
            print(f"Valor do produto: R$ {valor_produto:.2f}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto:.2f}")

    case _:
        print("Forma de pagamento inválida.")
