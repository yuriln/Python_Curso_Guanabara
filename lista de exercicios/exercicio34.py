try:
    salario = float(input('Qual o salario do funcionário: ')) 

    if salario <= 1250:
        aumento_abaixo_1250 = ((15/100) * salario) + salario
        print(f'Novo salário de {aumento_abaixo_1250}')

    else:
        salarionovo = ((10/100) * salario) + salario
        print(f'Novo salário de {salarionovo}')
except ValueError:
    print('Entrada inválida. Certifique-se de digitar um número válido.')

try:
    salario = float(input('Qual o salário do funcionário: '))

    if salario <= 1250:
        aumento = 0.15  # 15% de aumento para salários até 1250
    else:
        aumento = 0.10  # 10% de aumento para salários acima de 1250

    novo_salario = salario + (aumento * salario)

    print(f'Novo salário de {novo_salario:.2f}')
except ValueError:
    print('Entrada inválida. Certifique-se de digitar um número válido.')