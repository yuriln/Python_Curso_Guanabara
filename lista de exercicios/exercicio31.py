try:
    distancia = float(input('Qual a distância do sua viagem: '))

    if distancia <= 200:
        valor_ate_200km = distancia * 0.5
        print('Sua viagem de {:.0f} km custará {:.2f} $ '.format(distancia,valor_ate_200km))

    else:
        valor_apos_200km = distancia * 0.45
        print('Sua viagem de {:.0f} km custará {:.2f} $ '.format(distancia,valor_apos_200km))
except ValueError:
    print('Entrada inválida. Certifique-se de digitar um número válido.')
