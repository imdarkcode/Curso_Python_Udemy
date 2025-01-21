"""
Exercício

Crie uma função que multiplique todos os argumentos não nomeados
recebitos e retorne o total
"""

def multiplicarValor(*args):
    produto = 1
    for i in args:
        produto *= i
    return produto

print(multiplicarValor(7, 2, 3, 6))