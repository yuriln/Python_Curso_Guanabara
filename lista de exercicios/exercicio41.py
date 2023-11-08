try:
    idade = int(input('Digite a sua idade: '))

    if idade <= 9:
        categoria = 'mirim'
    elif idade <= 14:
        categoria = 'infantil'
    elif idade <= 19:
        categoria = 'junior'
    elif idade == 20:
        categoria = 'sênior'
    else:
        categoria = 'master'

    print(f'Sua categoria é {categoria}')

except ValueError: print('Digite um valor válido')