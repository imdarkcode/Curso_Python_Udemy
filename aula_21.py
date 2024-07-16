# Operador "or", se qualquer uma das condições for verdadeira a saída será verdadeira
a = True or True
print(f'{a = }')

b = True or False
print(f'{b = }')

c = False or False
print(f'{c = }')

entrada = input('Entrar[E] ou Sair[S]: ')
senha = input('Senha[1234]: ')

if (entrada == 'E' or entrada == 'e') and senha == '1234':
    print('Entrou')
else:
    print('Saiu')

# Dá para utilizar no input para verificar se o usuário deixa de digitar
senha = input('Senha: ') or 'Sem senha'
print(senha)