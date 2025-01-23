"""
Dicionários em Python
"""

# Primeira maneira de criar um dicionário

pessoa = {
    "nome": "Otávio",
    "idade": 18,
    "altura": 1.77,
    "endereço": {
        "rua": "Rua das flores",
        "numero": 145,
        "bairro": "Centro"
    }
}

print(pessoa["nome"])
print(pessoa["endereço"]["rua"])

# Segunda maneira de criar um dicionário

pessoa_2 = dict(nome = "Lisa", idade = 21, altura = 1.64, endereço = dict(rua = "Rua dos cravos", numero = 124, bairro = "Centro"))

print(pessoa_2["nome"])
print(pessoa_2["endereço"]["rua"])