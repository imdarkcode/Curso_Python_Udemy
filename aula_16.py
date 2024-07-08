# Para criar uma condição use a função "if", tudo o que estiver dentro da condição será executado se a condição for 
# verdadeira
continuar = input('Deseja continuar a operação [S/N]? ')

if continuar == 'S':
    print('Operação continuada')
elif continuar == 'N':
    print('Operação finalizada')
else:
    print('Resposta inválida')
