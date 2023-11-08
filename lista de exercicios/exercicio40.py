try:
    nota_1 = float(input('Insira a primeira nota:  '))
    nota_2 = float(input('Insira a sugunda nota:  '))

    media = (nota_1 + nota_2) / 2

    if media < 5:
        print(f'Sua média é {media}, você está reprovado')

    elif media >= 5 and media <= 6.9:
        print(f'Sua média é {media}, você está de recuperação')
    else:
        print(f'Sua média é {media}, você está aprovado')

except ValueError: 
    print('Digite um valor valido') 

#     try:
#     nota_1 = float(input('Insira a primeira nota: '))
#     nota_2 = float(input('Insira a segunda nota: '))

#     media = (nota_1 + nota_2) / 2

#     if media < 5:
#         situacao = 'reprovado'
#     elif media <= 6.9:
#         situacao = 'em recuperação'
#     else:
#         situacao = 'aprovado'

#     print(f'Sua média é {media}, você está {situacao}')
# except ValueError:
#     print('Digite um valor válido')