preco = float(input('Insira o valor do produto: '))

perc_desco = float(input('Digite o percentual do desconto: '))
desconto = preco - ((perc_desco / 100) * preco)

print(f'O produto com desconto de {perc_desco} % é: {desconto}')