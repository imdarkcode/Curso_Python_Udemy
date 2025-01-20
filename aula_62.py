"""
Introdução a função (def)

Funções são trechos de cógido usados para
replicar determinada ação ao longo do código

Eles podem receber valores como parâmetros e podem
retornar outro valor
"""

# Exemplo de função que retorna a soma de 2 valores

def calcularSoma(valor_1, valor_2):
    return valor_1 + valor_2

valor_1 = 10
valor_2 = 12

print(calcularSoma(10, 12))

# Exemplo de função de mostrar mensagem

def mostrarNome(nome):
    print(f"Olá, {nome}")

mostrarNome("Otávio")
