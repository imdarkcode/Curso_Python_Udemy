# Desempacotamento

# Utilizando variáveis para separar os valores de uma list

# Para isso funcionar a quantidade de variáveis precisa ser igual a quantidade de valores no array

nome1, nome2, nome3 = ['João', 'Eric', 'Felipe']
print(nome2)

# É possivel criar uma variavel de "resto" para armazenar os demais valores, utilizando o símbolo de *

# Em python é comum utiizar o _ para representar uma variável que não será usada

nome1, *_ = ['João', 'Eric', 'Felipe']
print(nome1)

