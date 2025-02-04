"""
Métodos úteis do set
"""

conjunto_1 = set()

# add(): Adicionar uma valor

conjunto_1.add(5)
print(conjunto_1)

# update(): Atualizar o set

conjunto_1.update((7, 8, 4))
print(conjunto_1)

# discard(): Eliminar um valor

conjunto_1.discard(8)
print(conjunto_1)

# clear(): Limpar o set

conjunto_1.clear()
print(conjunto_1)