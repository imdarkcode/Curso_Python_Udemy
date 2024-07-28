# Exercício

# Gerar uma nova string a partir do while

string = 'DarkCode'
tamanho_string = len(string)
contador = 0
nova_string = ''

while contador < tamanho_string:
    nova_string += '|' + string[contador] + '|'
    contador += 1

print(nova_string)