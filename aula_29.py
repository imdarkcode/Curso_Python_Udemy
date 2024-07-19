# Boas práticas de programação

# Criar variáveis com letras maiúsculas para indicar que a variável é constante (seu valor não muda)

VEL_MAX = 10
VEL_MIN = 3
GRAVIDADE = 3.5

# Simplificar condições utilizando variáveis

tocando_chao = True
tecla_apertada = True
pular = tocando_chao and tecla_apertada

if pular:
    print('Personagem pulou')

