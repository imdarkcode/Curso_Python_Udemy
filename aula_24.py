# Interpolação de strings "%"
# s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'Otávio'
preco = 45.98
interpolacao = '%s, o preço é R$%.4f' % (nome, preco)
print(interpolacao)
print('O hexdecimal de %d é %06x' % (4890,4890)) 