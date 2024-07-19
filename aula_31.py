# Flag - Marcar se executou determinada parte do código
# "None" representa um dado nulo
# "is" tem a mesma função do "=="

valor = 1
entrou_na_condicao = None

if valor:
    entrou_na_condicao = True
    print('Valor existe')
else:
    print('Valor não existe')

print(f'Entrou na condição: {entrou_na_condicao is not None}')