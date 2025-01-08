# Tipo tuple: funciona igual uma list com a diferença que seus valores não poderão ser alterados

# Para criar um tuple pode usar parenteses ou deixar os valores sem nada em volta

nomes = ('José', 'Marcos', 'Leonardo')
print(nomes[1])

# Também é possivel converter tuple para list ou vice-verse

nomes_list = list(nomes)
nomes_tuple = tuple(nomes_list)