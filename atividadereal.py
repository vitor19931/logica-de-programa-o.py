import os
os.system("cls || clear")

valor_produto = float(input("Informe o valor do produto: "))
print("Formas de pagamento")
print("1 - pagamento a vista")
print("2 - pagamento a prazo")
forma_pagamento = float(input("Escolha a forma de pagamento  (1 ou 2): "))

match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print("\n pagamento a vista:")
        print(f"valor do produto: R${valor_produto:.2f}")
        print("forma de pagamento a vista")
        print(f"valor do desconto: R${desconto:.2f}")
        print(f"total a pagar: R${total:.2f}")
    case 2:
            parcelas = int(input("Informe a quantitade de parcelas (ate 6): "))
            if parcelas > 6:
                 print("O numero de parcelas estão invalidos, não podemos realizar o pagamento")
            else:
                  valor_parcela = valor_produto / parcelas
                  print("\n pagamenro a prazo:")
                  print(f"valor do produto: R${valor_produto:.2f}")
                  print("forma de pagamento a prazo: ")
                  print(f"quantidade de parcelas: R${parcelas:.2f}")
                  print(f"valor das parcelas: R${valor_parcela:.2f}")
                  print(f"total a prazo: R${valor_produto:.2f}")
    case _:
          print("pagamento invalido")              