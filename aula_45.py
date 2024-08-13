# Exercício

# Faça um jogo para o usuário adivinhar qual a palavra secreta.
#   - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
#   o usuário digitar apenas uma letra.
#   - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
#   na palavra secreta.
#   - Se a letra digitada estiver na palavra secreta; exiba a letra;
#   - Se a letra digitada não estiver na palavra secreta; exiba *.
#   Faça a contagem de tentativas do seu usuário.

palavra_secreta = 'darkcode'
tentativas = 5
letras_descobertas = ''
palavra_escondida = '*' * len(palavra_secreta)

while tentativas > 0:
    print(palavra_escondida)
    print(f'Tentativas = {tentativas}')
    letra = input('Digite uma letra: ').lower()

    if letra in letras_descobertas:
        print('Letra já foi digitada')
    else:
        letras_descobertas += letra

        if letra in palavra_secreta:
            print(f'Letra "{letra.upper()}" está certa')

            palavra_escondida = ''
            for i in palavra_secreta:
                if i in letras_descobertas:
                    palavra_escondida += i
                else:
                    palavra_escondida += '*'
        else:
            print(f'Letra "{letra.upper()}" está incorreta')
            tentativas -= 1
        
    if palavra_secreta in palavra_escondida:
        print('Você ganhou')
        break
else:
    print('Você perdeu')
