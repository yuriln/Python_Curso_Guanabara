salario = float(input('Insira o valor do salario: '))

perc_aumento = float(input('Digite o percentual do aumento: '))
novo_salario= salario + ((perc_aumento / 100) * salario)

print(f'O salário com aumento de {perc_aumento} % é: {novo_salario}')