# A função "format" também formata uma string com base nos parâmetros que vocês utiliza. Obs: Caso as chaves estejam vazias ele pedagá pela ordem dos parâmetros
a = 'A'
b = True
c = 1.1
linha = 'a = {} \nb = {} \nc = {}'
print(linha.format(a, b, c))

# Também da para utilizar a posição dos parâmetros para chamá-los na função
linha = 'a = {0} \na = {0} \na = {0}'
print(linha.format(a, b, c))

# Também da para nomear os parametros ao invés de chamá-los pela posição
linha = 'a = {letra} \nb = {valor_bool} \nc = {numero_decimal}'
print(linha.format(letra = a, valor_bool = b, numero_decimal = c))