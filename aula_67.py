"""
Empacotamento de argumentos

Empacotar os argumentos converte eles em uma lista que
dentro da função pode ser desempacotada, dessa forma a função
pode ser executada sem uma quantidade específica de argumentos

Normalmente é usado *args que significa "Argumentos não nomeados"
"""

# Nesse exemplo, a função funcionará com qualquer quantidade de argumentos

def somarValores(*args):
    soma = 0
    for i in args:
        soma += i
    return soma

print(somarValores(78, 56, 41, 20))
print(somarValores(47, 20))
print(somarValores(13, 46, 47, 11, 1))