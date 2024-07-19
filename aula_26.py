# Fatiamento de strings

var = 'Olá mundo'
#      012345678

print(var[4:9]) # O primeiro parametro é qual caracter irá começar
print(var[0:2]) # O segundo é até qual caracter irá pegar
print(var[0:9:2]) # O último parâmetro é quantos caracteres ele irá pular
print(var[2:]) # Caso omita algum parâmetro o código irá pegarpor padrão [início:final:1]
print(var[-8:-2]) # Também funciona com índices negativos
print(var[::-1]) # Caso o último parâmetro seja negativo a string se inverte

# Função "len()"
quantidade = len(var) # Conta a quantidade de caracteres de uma string
print(quantidade)

