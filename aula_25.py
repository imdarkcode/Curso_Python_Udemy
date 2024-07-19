# Formatação com f-string

# Espaçamento
var = 'ABC'
print(f'{var:}.')
print(f'{var: >10}') # Esquerda
print(f'{var: <10}') # Direita
print(f'{var: ^10}') # Centro

print(f'{var:->10}') # Preenchimento com caracter

# Números
print(f'{45154.479543}')
print(f'{45154.479543:.1f}') # Arredondar
print(f'{45154.479543:,f}') # Seperar a casa do milhar
print(f'{45154.479543:+f}') # Mostrar sinal caso seja positivo

# Hexadecimal
print(f'{1500:08x}') # Hexadecimal minúsculo
print(f'{1500:08X}') # Hexadecimal maiúsculo
