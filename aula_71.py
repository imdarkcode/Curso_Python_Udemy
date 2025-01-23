"""
Higher Order Functions

Funções que podem receber e retornar outras funções
"""

def soma(x, y):
    return x + y

def executar(funcao, *args):
    return funcao(*args)

print(executar(soma, 10, 54))

