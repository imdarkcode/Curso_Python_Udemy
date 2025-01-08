# Exercício

"""
Faça uma lista de comprar om listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o prograa quebre com
erros de índices iexistentes na lista.
"""

import os

produtos = []

while True:
    print("Lista de compras")
    print("Informe a ação que deseja executar")
    print("[1] Adicionar novo produto")
    print("[2] Remover produto")
    print("[3] Listar produtos")
    print("[4] Sair")
    opcao = input()

    try:
        opcao_int = int(opcao)

        if opcao_int == 1:
            os.system("cls")
            produto = input("Informe o nome do produto: ")
            produtos.append(produto)
        elif opcao_int == 2:
            os.system("cls")
            if len(produtos) >= 1:
                indice = int(input("Informe o código do produto: "))
                del produtos[indice]
            else:
                print("Não há produtos para remover")
        elif opcao_int == 3:
            os.system("cls")
            if len(produtos) >= 1:
                for i, p in enumerate(produtos):
                    print(f"{i} - {p}")
            else:
                print("Não há produtos para listar")
        elif opcao_int == 4:
            break
        else:
            os.system("cls")
            print("Opção não identificada")
    
    except:
        os.system("cls")
        print("Opção não identificada")