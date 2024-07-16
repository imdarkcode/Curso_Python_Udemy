# Operador "not", inverte a expressão
a = not True
print(f'{a = }')

b = not False
print(f'{b = }')

senha = input('Senha: ')

if not senha:
    print('Não digitou nada')
else:
    print(f'Digitou {senha}')