# Gerador de CPF

import random

contador = 10
soma = 0
primeiro_digito = 0
nove_digitos = ""

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Primeiro digito

for valor in nove_digitos:
    soma += int(valor) * contador
    contador -= 1

resto = (soma * 10) % 11

if resto <= 9:
    primeiro_digito = resto
else:
    primeiro_digito = 0

# Segundo digito

dez_digitos = nove_digitos + str(primeiro_digito)
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

print(nove_digitos + str(primeiro_digito) + str(segundo_digito))
