# Dados Imutáveis: str, int, float, bool

string = "Texto"

try:
    string[2] = 's'
    print(string)
except:
    print('Não é possível modificar o dado')

# Métodos de string

print(string.upper()) # Deixa tudo maiúnculo
print(string.lower()) # Deixa tudo minúsculo
print(string.zfill(7)) # Preenche com zeros à esquerda
