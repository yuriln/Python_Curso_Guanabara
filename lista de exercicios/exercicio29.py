vel = int(input('Qual a velocidade do carro em km/h na estrada? '))

if vel > 80:
    multa = (vel - 80) * 7
    print("multa de {} $".format(multa))

else:
    print('Velocidade {} km/h permitida'.format(vel))