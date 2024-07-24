# Utilizar o "continue" para pular uma repetição

contador = 0

while contador < 10:
    contador += 1
    if contador == 4:
        continue # Pula o resto do código e repete a execução
    print(contador)

print('Fim da repetição')