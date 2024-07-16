# Operador lógico "and", todas as condições precisam ser verdadeiras, se uma das condições não for verdadeira a saída
# será falsa
a = True and True
print(f'{a = }')

b = True and False
print(f'{b = }')

c = False and False
print(f'{c = }')

entrada = input('Entrar[E] ou Sair[S]: ')
senha = input('Senha[1234]: ')

if entrada == 'E' and senha == '1234':
    print('Entrou')
else:
    print('Saiu')