try:
    r1 = float(input('Digite a distancia entre o ponto AB: '))
    r2 = float(input('Digite a distancia entre o ponto CD: '))
    r3 = float(input('Digite a distancia entre o ponto EF: '))

    if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
        trianguformado = 'Triângulo formado'
        print(f'{trianguformado}')

        if r1==r2==r3: print('Equilátero, todos os lados iguais')
        elif r1 != r2 and r1 != r3: print('Escaleno, todos os lados diferentes')
        else: print('Isosceles, doi lados iguais') 

    else: print('Essas valores não formam um triangulo')

except ValueError: print('Entrada inválida. Certifique-se de digitar um número válido.')




# r1 == r2 or r2 == r3 or r3 == r1: print('Isósceles')