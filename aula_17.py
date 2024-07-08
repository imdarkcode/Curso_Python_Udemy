# A função "if" sempre irá verificar se a condição for verdadeira (True) mesmo que não seja escrita junto ao "if"
condicao = True

if condicao:
    print('Condição verdadeira')
else:
    print('Condição falsa')

# A função sempre ira tentar converter a condição para valor do tipo bool
string = ""
print(bool(string))

if string:
    print('Foi digitado algo na string')
else:
    print('A string está vazia')