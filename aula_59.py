"""
Operação ternária (estrutura condicional em uma linha)
<valor> if <condicao> else <outro valor>
"""

valor = 7
verificador = "Par" if valor % 2 == 0 else "Ímpar"
print(verificador)

# É possível utilizar mais de uma condição

valor = 0
verificador = "Neutro" if valor == 0 else "Par" if valor % 2 == 0 else "Ímpar"
print(verificador)