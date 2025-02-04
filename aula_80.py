"""
Operadores com set
"""

conjunto_1 = {1, 2, 3}
conjunto_2 = {2, 3, 4}

# união "|"

conjunto_3 = conjunto_1 | conjunto_2
print(conjunto_3)

# intersecção "&"

conjunto_4 = conjunto_1 & conjunto_2
print(conjunto_4)

# diferença "-"

conjunto_5 = conjunto_1 - conjunto_2
print(conjunto_5)

# diferença simétrica "^"

conjunto_6 = conjunto_1 ^ conjunto_2
print(conjunto_6)
