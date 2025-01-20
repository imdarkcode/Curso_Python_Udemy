"""
Valores padrão para parâmetros

Caso não seja enviado nenhum parâmetro o valor
padrão é usado
"""

# Nessa função, mesmo que não seja passado o valor de z a função não quebra
# É recomendado usar None ao invés de 0, pois fica mais fácil de verificar se o parâmetro foi passado ou não

def calcularSoma(x, y, z = None):
    if z is not None:
        print(f"{x} + {y} + {z} = {x + y + z}")
    else:
         print(f"{x} + {y} = {x + y}")

calcularSoma(5, 10)
calcularSoma(84, 12, 45)
calcularSoma(14, 79, 0)