"""
Escopo de funções em Python

Escopo global: É onde o código pode ser acessado sem nenhuma
chamada, quando uma variável é declarada ela funcionará no código todo

Escopo local: São locais onde o código só acessa caso for
chamado, quando uma variável é declarada ela só funcionará
dentro desse local
"""

# Escopo global
# AS variáveis existem no código inteiro

x = 10
y = 45

def soma():
    print(f"{x} + {y} = {x + y}")

def subtracao():
    print(f"{y} - {x} = {y - x}")

# Escopo local
# As variáveis só existem dentro dessa função

def multiplicacao():
    x = 2
    y = 5
    print(f"{x} x {y} = {x * y}")

soma()
subtracao()
multiplicacao()