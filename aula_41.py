# While/else

string = 'DarkCode'
contador = 0

while contador < len(string):
    print(string[contador])

    contador += 1
else: # Será executado sempre no final do while a menos que seja dado um "break"
    print('O else foi executado')

# Exemplo com break

contador = 0

while contador < len(string):
    print(string[contador])

    contador += 1

    if contador == 4:
        break
else: # Não será executado
    print('O else foi executado')