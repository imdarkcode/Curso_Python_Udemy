"""
Exercício

Crie uma função que retone se um número é par ou ímpar
"""

def parImpar(valor):
    if valor % 2 == 0:
        return("par")
    return("ímpar")

valor = 7
print(f"O valor {valor} é {parImpar(valor)}")