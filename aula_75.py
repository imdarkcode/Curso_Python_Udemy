"""
Manipulando chaves e valores em dicionários
"""

pessoa = {}

# Definir uma chave

chave = "nome"
pessoa[chave] = "Otávio"

# Mostrar valor na chave

print(pessoa[chave])

# Apagar chave

del pessoa[chave]
print(pessoa)

# Verificar se uma chave existe

if pessoa.get("idade") is None:
    print("Essa chave não existe")
else:
    print("Essa chave existe")