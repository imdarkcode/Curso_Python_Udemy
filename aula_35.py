# A repetição nunca será executada se a condição for falsa

while False:
    print('ABC') # Não será executado

print('Fim da repetição')

# Utilizar uma variável de contador para manipular a quantidade de repetições

contador = 0

while contador < 10:
    contador += 1
    print(contador)

print('Fim da repetição')
