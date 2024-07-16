# Todos os dados de string são iteráveis (pode ser serado por itens), cada caracter possui um índice (posição)
string = 'Pudim'
print(string[2])

# Operador "in", verifica se há algo entre uma expressão
a = 'i' in 'Otávio'
print(f'{a = }')

b = '7' in '12345'
print(f'{b = }')

# Operador "not in", verifica se não há algo entre uma expressão
c = 'v' not in 'Otávio'
print(f'{c = }')

d = '10' not in '12345'
print(f'{d = }')

nome = input('Digite seu nome: ')
letra = input('Digite a letra que deseja encontrar: ')

if letra in nome:
    print(f'{letra} está no seu nome')
else:
    print(f'{letra} não está no seu nome')


