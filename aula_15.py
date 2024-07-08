# A função "input" para o código e pede para o usuário digitar
input('Digite algo: ')

# Use uma variavel para salvar o valor do input para o tipo string
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')

# Para saber o nome da variável junto com seu valor usando um "=" depois da variável
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome=}')

# Para salvar outros tipos de variáveis do input precisa fazer a conversão, porém caso o usuário não digite o tipo 
# correto da variável, o programa quebra
string = input('Variável do tipo string: ')
inteiro = int(input('Variável do tipo int: '))
boolean = bool(input('Variável do tipo bool: '))
decimal = float(input('Variável do tipo float: '))
print(f'String: {string}\nInt: {inteiro}\nBool: {boolean}\nFloat: {decimal}')

