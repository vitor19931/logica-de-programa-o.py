familia = []
total_familia = 0
maior_salario = 0
menor_salario = 0
media_salario = 0
media_numero_filhos = 0

while True:
    print(""" Menu:
    1. Adicionar FAMILIA
    2. Exibir relatório
    """)
    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            salario = float(input("Salário: "))
            numero_filhos = int(input("Número de filhos: "))

            if salario < menor_salario or menor_salario == 0:
                menor_salario = salario
            if salario > maior_salario:
                maior_salario = salario

            media_salario = (media_salario + salario) / 2
            media_numero_filhos = (media_numero_filhos + numero_filhos) / 2
            total_familia += 1

        case "2":
            if total_familia == 0:
                print("Nenhuma família cadastrada.")
            else:
                print(f"Menor salário: {menor_salario}")
                print(f"Maior salário: {maior_salario}")
                print(f"Média de salário: {media_salario:.2f}")
                print(f"Média de número de filhos: {media_numero_filhos:.2f}")
            print("Saindo...")
            break

