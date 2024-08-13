# Métodos de list

# Append - Acrescenta um elemento no final
lista = [10, 20, 30, 40]
lista.append(50)
print(lista)

# Pop - Remove o ultimo elemento ou do índice inserido
lista.pop()
print(lista)

# Del - Remove o elemento do índice inserido
del lista[2]
print(lista)

# Clear - Limpa a lista
lista.clear()
print(lista)

# Insert - Inseri um elemento ao índice escolhido
lista = [10, 20, 30, 40]
lista.insert(1, 15)
print(lista)

# + - Concatenar listas
lista_2 = [50, 60, 70]
lista_3 = lista + lista_2
print(lista_3)

# Extend - Acrescenta uma lista dentro de outra
lista.extend(lista_2)
print(lista)