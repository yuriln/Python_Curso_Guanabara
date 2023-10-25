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
