import os
import time
from dataclasses import dataclass

def limpar_tela():
    os.system("cls || clear")

lista_clientes = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

def lista_vazia(lista):
    if not lista:
        print("\n❌ Não há clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista):
    print("\n=== Adicionar Cliente ===")
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    lista.append(Cliente(nome, email, telefone))
    print("\n✅ Cliente adicionado com sucesso!")

def buscar_cliente_por_email(lista, email_busca):
    email_busca = email_busca.lower()

    for cliente in lista:
        if cliente.email.lower() == email_busca:
            return cliente

    return None

def mostrar_todos_clientes(lista):
    if lista_vazia(lista):
        return
    
    print("\n=== Lista de Clientes ===")
    for cliente in lista:
        cliente.mostrar_dados()
        print("------------------------")

def atualizar_cliente(lista):
    if lista_vazia(lista):
        return

    mostrar_todos_clientes(lista)
    email_busca = input("\nDigite o e-mail do cliente que deseja atualizar: ")

    cliente = buscar_cliente_por_email(lista, email_busca)

    if not cliente:
        print("❌ Cliente não encontrado.")
        return

    print("\n=== Atualizar Dados ===")
    novo_nome = input(f"Novo nome (Atual: {cliente.nome}) ou ENTER para manter: ")
    novo_email = input(f"Novo e-mail (Atual: {cliente.email}) ou ENTER para manter: ")
    novo_telefone = input(f"Novo telefone (Atual: {cliente.telefone}) ou ENTER para manter: ")

    if novo_nome.strip():
        cliente.nome = novo_nome
    if novo_email.strip():
        cliente.email = novo_email
    if novo_telefone.strip():
        cliente.telefone = novo_telefone

    print("\n✅ Cliente atualizado com sucesso!")

def excluir_cliente(lista):
    if lista_vazia(lista):
        return

    mostrar_todos_clientes(lista)
    email_busca = input("\nDigite o e-mail do cliente que deseja excluir: ")

    cliente = buscar_cliente_por_email(lista, email_busca)

    if cliente:
        lista.remove(cliente)
        print(f"\n🗑 Cliente '{cliente.nome}' excluído com sucesso!")
    else:
        print("\n❌ Cliente não encontrado.")

# ============================
# MENU PRINCIPAL
# ============================

while True:
    print("""
==== Gerenciamento de Clientes ====

1. Adicionar cliente
2. Mostrar todos os clientes
3. Atualizar cliente
4. Excluir cliente
0. Sair
""")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("❌ Entrada inválida! Digite um número.")
        continue

    if opcao == 1:
        adicionar_cliente(lista_clientes)
    elif opcao == 2:
        mostrar_todos_clientes(lista_clientes)
    elif opcao == 3:
        atualizar_cliente(lista_clientes)
    elif opcao == 4:
        excluir_cliente(lista_clientes)
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("❌ Opção inválida!")

    time.sleep(4)
    limpar_tela()
