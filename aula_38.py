# While detro de while

linha = 1
coluna = 1

while linha <= 5:
    while coluna <= 5:
        print(f'{linha = } | {coluna = }')
        coluna += 1
    linha += 1
    coluna = 1