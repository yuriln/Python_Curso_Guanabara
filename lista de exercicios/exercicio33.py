try:
    num1 = int(input('Insira um numero: '))
    num2 = int(input('Insira um segundo número: '))
    num3 = int(input('Insira um terceiro número: '))

    if num1 >= num2 and num1 >= num3:
        print('O maior número é o {}.'.format(num1))

    elif num2 >= num1 and num2 >= num3:
        print('O maior número é o {}.'.format(num2))

    else:
        print('O maior número é o {}.'.format(num3))

except ValueError:
    print('Entrada inválida. Certifique-se de digitar um número válido.')

# código refatorado utlizando a função max
# try:
#     num1 = int(input('Insira um número: '))
#     num2 = int(input('Insira um segundo número: '))
#     num3 = int(input('Insira um terceiro número: '))

#     maior_numero = max(num1, num2, num3)

#     print('O maior número é o {}.'.format(maior_numero))

# except ValueError:
#     print('Entrada inválida. Certifique-se de digitar um número válido.')