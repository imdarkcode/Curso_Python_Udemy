# Exercício

# Calculadora while
while True:

    valor_1 = input('Digite o primeiro valor: ')
    valor_2 = input('Digite o segundo valor: ')

    numeros_validos = None

    try:
        valor_1_inteiro = int(valor_1)
        valor_2_inteiro = int(valor_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Valores Inválidos')
        continue

    operacao = input('Digite a operação [+,-,*,/]: ')
    operadores_permitidos = '+-*/'

    if operacao not in operadores_permitidos:
        print('Operação Inválida')
        continue

    if operacao == '+':
        resultado = valor_1_inteiro + valor_2_inteiro
    elif operacao == '-':
        resultado = valor_1_inteiro - valor_2_inteiro
    elif operacao == '*':
        resultado = valor_1_inteiro * valor_2_inteiro
    else:
        resultado = valor_1_inteiro / valor_2_inteiro

        print(f'Resultado: {resultado}')

    while True:
        sair = input('Deseja continuar [S/N]: ')

        if sair:
            if sair.upper() == 'N':
                quit()
            elif sair.upper() == 'S':
                break
            else:
                print('Resposta Inválida')
        else:
            print('Resposta Inválida')