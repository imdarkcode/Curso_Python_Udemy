nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    idade = int(idade)
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print(f'Você deixou campos vazios')