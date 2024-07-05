# O sinal "+" irá concatenar valores de string e somar valores numéricos. Obs: Só funciona com tipos de dados iguais
print('a' + 'b')
print(1 + 2.5)

# No caso de dados com tipo boolean o "+" entende "True" como 1 e "False" como 0
print(True + False)

# A função "str()" converte dados para o tipo string
print(str(1) + str(1))

# A função "int()" converte dados para o tipo inteiro
print(int(True))

# A função "float()" converte dados para o tipo decimal
print(float(1))

# A função "bool()" converte dados para o tipo boolean. Obs: String vazia é considerada "False"
print(bool(''))
print(bool('a'))