# Exercício

# Crie um programa que diga qual letra se repete mais na string

string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
tamanho_string = len(string)
contador = 0
maior_quantidade = 0

while contador < tamanho_string:
    string = string.lower()
    letra = string[contador]

    contador += 1

    if letra == ' ':
        continue

    quantidade_letras = string.count(letra)

    if quantidade_letras > maior_quantidade:
        maior_quantidade = quantidade_letras
        letra_mais_repetida = letra

print(f'Letra mais repetidao: {letra_mais_repetida}')


