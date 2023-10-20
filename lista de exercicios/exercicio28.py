import random

num=int(input('Insira um número de 0 a 5:'))

aleatorio = random.randint(0,5)

print(aleatorio)

print('Voce venceu' if num ==aleatorio else 'O computador venceu')