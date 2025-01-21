"""
Retornando valores em funções
"""

# Exemplo de função que retorna um valor
# Nesse caso a função devolve o resultado da soma

def calcularSoma(x, y):
    return x + y

print(calcularSoma(5, 74))

# Toda função retorna apenas um valor mesmo que tenha mais de um return
# Assim que a execução chega no return o rsto do código da função é desconsiderado

def parImpar(x):
    if x % 2 == 0:
        return "par"
    print("a")
    return "impar"

print(parImpar(4))

