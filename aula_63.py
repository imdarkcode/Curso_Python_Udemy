"""
Argumentos nomeados e posicionais (não nomeados) em funções

Argumentos não nomeados: São argumentos que depende da posição
que são passados como parâmetros

Argumnetos nomeados: São argumentos são definidos com um nome
e o sinal de igual
"""

# Exemplo de função com argumentos posicionais
# Se mudar a ordem dos argumnetos o resultado muda

def calcularSoma(x, y):
    print(x + y)

calcularSoma(5, 10)

# Exemplo de função com argumentos nomeados
# Mesmo que mude a ordem do x e y o resultado se mantem o mesmo

def calcularSoma(x, y):
    print(x + y)

calcularSoma(y = 5, x = 10)