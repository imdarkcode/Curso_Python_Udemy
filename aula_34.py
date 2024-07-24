# Estrutura de repetição "while"

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    
    if not nome:
        break # Interrompe a repetição mais próxima
    else:
        print(f'Seu nome é {nome}')