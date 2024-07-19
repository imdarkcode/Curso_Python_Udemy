# Try except - detectar erros de execução

numero = input('Digite um valor: ')

try:
    numero_int = int(numero) # Caso essa linha dê um erro ele irá direto para o except em vez de parar o código
    print(numero_int)
except:
    print('Isso não é um valor')