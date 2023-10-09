from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir:{hi:.2f}')