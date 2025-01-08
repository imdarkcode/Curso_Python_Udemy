# Enumerate: uma função que cria um enumerador para uma lista

nomes = ['Maria', 'Carla', 'Vivian']
nomes_enumerados = enumerate(nomes)

# Para mostrar a lista ou tupla enumerada é preciso fazer a conversão

print(list(nomes_enumerados))

# Com o atributo start= é possível definir o número que começará a contagem

nomes_enumerados = enumerate(nomes, start=12)
print(list(nomes_enumerados))

# Usando for para mostrar o índice junto ao item, o python ja desempacota o indice do valor

for indice, nome in enumerate(nomes):
    print(f"{indice} - {nome}")
