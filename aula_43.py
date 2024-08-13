# Laço de repetição "for"

# Usado quando já sabe a quantidade de vezes precisará repetir

# O "while" é mais usado quando não sabe quantas vezes irá repetir

# Exemplo de código com "while"
string = 'Texto'
contador = 0

while contador < len(string):
    print(string[contador])
    contador += 1

# Mesmo código utilizando o "for"
for letra in 'Texto': # Nesse caso a variável "i" pegará o valor de cada letra da string
    print(letra)

# Lembre-se: "in" significa pegar algo que pertence a um dado

