# Exercícios

# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

numero = input('Digite um número: ')

try:
    numero_int = int(numero)
    par = numero_int % 2 == 0

    if par:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print('Não foi digitado um número inteiro')

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = input('Digite a hora atual: ')

try:
    hora_int = int(hora)
    dia = hora_int >= 0 and hora_int <= 11
    tarde = hora_int >= 12 and hora_int <= 17
    noite = hora_int >= 18 and hora_int <= 23

    if dia:
        print(f'Bom dia')
    elif tarde:
        print(f'Boa tarde')
    elif noite:
        print(f'Boa noite')
except:
    print('Não foi digitado uma hora')

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome = input('Digite seu primeiro nome: ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) == 5 or len(nome) == 6
nome_grande = len(nome) > 6

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
elif nome_grande:
    print('Seu nome é grande')