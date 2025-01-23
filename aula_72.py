"""
Closure

Adiar a execução de uma função, fazendo o código salvar os argumentos
já definidos
"""

def cumprimento(saudacao):
    def cumprimentar(nome):
        return f"{saudacao}, {nome}!"
    return cumprimentar

bom_dia = cumprimento("Bom dia")
boa_tarde = cumprimento("Boa tarde")
boa_noite = cumprimento("Boa noite")

print(bom_dia("Otávio"))
print(boa_noite("Alisson"))
print(boa_tarde("Eick"))