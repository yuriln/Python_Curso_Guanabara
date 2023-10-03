altura = float(input('Insira a altua da parede em metros: '))
largura = float(input('Insira a largura da parede em metros:'))

area = (altura * largura)
tinta_utl = area / 2
print('Para pintar uma área de {:3} m², precisamos de {:.3} litos de tinta.'.format(area, tinta_utl))