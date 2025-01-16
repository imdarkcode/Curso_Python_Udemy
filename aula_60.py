"""
Exercício: Validador de CPF

Calculando o primeiro digito:

    - Coletar o CPF
    - Colete os 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva
começando de 10
    - Somar os resultados
    - Multiplicar o resultado por 10
    - Obter o resto da divisão da conta por 11
    - Se o resultado for maior que 9, o primeiro digito será 0,
se não será ele mesmo

Calculando o segundo digito:

    - Colete os 9 primeiros dígitos do CPF e o primeiro
digito obtido multiplicando cada um dos valores por uma contagem
regressiva começando de 11
    - Somar os resultados
    - Multiplicar o resultado por 10
    - Obter o resto da divisão da conta por 11
    - Se o resultado for maior que 9, o segundo digito será 0,
se não será ele mesmo
"""

while True:
    contador = 10
    soma = 0
    primeiro_digito = 0
    cpf = input("Informe uma CPF para validar: ")

    try:
        # Primeiro dígito

        cpf_formatado = cpf.replace('.', '').replace('-', '')
        nove_digitos = cpf_formatado[:9]

        for valor in nove_digitos:
            soma += int(valor) * contador
            contador -= 1

        resto = (soma * 10) % 11

        if resto <= 9:
            primeiro_digito = resto
        else:
            primeiro_digito = 0

        # Segundo digito

        dez_digitos = cpf_formatado[:9] + str(primeiro_digito)
        contador = 11
        soma = 0

        for valor in dez_digitos:
            soma += int(valor) * contador
            contador -= 1

        resto = (soma * 10) % 11

        if resto <= 9:
            segundo_digito = resto
        else:
            segundo_digito = 0

        if primeiro_digito == int(cpf_formatado[-2]) and segundo_digito == int(cpf_formatado[-1]):
            print("CPF válido")
        else:
            print("CPF inválido")

        continuar = input("Deseja digitar um novo CPF [s]Sim ou [n]Não?")

        if continuar == "n":
            break

    except:
        print("Formato do CPF incorreto")

