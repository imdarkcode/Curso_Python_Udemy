"""
Métodos úteis dos dicionarios em Python
"""

pessoa = {
    "nome": "Otávio",
    "idade": 18,
    "altura": 1.77,
}

# len(): retorna a quantidade de chaves no dicionários

print(len(pessoa))

# keys(): retorna as chaves do dicionário

print(pessoa.keys())

# values(): retorna os valores das chaves do dicionário

print(pessoa.values())

# items(): retorna as chaves e os valores do dicionário

print(pessoa.items())

# setdefault(): adiciona um valor padrão caso a chave não existir

pessoa.setdefault('peso', 0.0)
print(pessoa['peso'])

# copy(): retorna uma cópia do dicionário

mesma_pessoa = pessoa.copy()
print(mesma_pessoa)

# get(): pega o valor de uma chave do dicionário ou retorna None ou um valor que você pode atribuir caso ela não existir

print(pessoa.get('nome'))
print(pessoa.get('sobrenome', "Não existe"))

# pop(): retira o valor e a chave de um dicionário, podendo ser salvo em outro lugar

nome = pessoa.pop('nome')
print(nome)
print(pessoa)

# popitem(): retira a ultima chave do dicionário, podendo ser salvo em outro lugar

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

# update(): atualiza o dicionário

pessoa.update({
    'nome': "Otávio Sudano",
})
print(pessoa)
