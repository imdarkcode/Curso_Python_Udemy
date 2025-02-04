"""
Exercício

Crie uma função que encontre o primeiro duplicado considerando
o segundo número como a duplicação. Retorne a duplicação considerada.

Requisitos:
    A ordem donúmero duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicad em si.
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Não tem duplicados (retorne -1)
"""

lista_numeros_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 5, 5, 7, 6, 4, 1, 8],
    [10, 4, 7, 9, 4, 10, 6, 7, 2],
    [8, 10, 1, 5, 3, 9, 6, 4, 2],
    [1, 3, 3, 1, 10, 5, 5, 7, 3],
    [1, 3, 7, 1, 4, 1, 6, 8, 3],
    [10, 4, 1, 3, 8, 10, 6, 5, 2],
    [3, 3, 5, 1, 4, 8, 6, 7, 2],
]

for lista in lista_numeros_inteiros:
    numeros = set()
    repetidos = []

    for item in lista:
        if item not in numeros:
            numeros.add(item)
        else:
            repetidos.append(item)

    if repetidos:
        print(repetidos[0])
    else:
        print(-1)


