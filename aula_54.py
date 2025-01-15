# Imprecisão de valores tipo double

soma = 0.1 + 0.7
print(soma)

# Há três maneiras de resolver esse problema

# Usando f-string

print(f"{soma:.1f}")

# Usando a função round()

print(round(soma, 2))

# Usando o módulo decimal

import decimal

soma = decimal.Decimal("0.1") + decimal.Decimal("0.7")
print(soma)