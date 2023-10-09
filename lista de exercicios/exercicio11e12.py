import random
n1 = input('Nome do 1º aluno: ')
n4 = input('Nome do 1º aluno: ')
n3 = input('Nome do 1º aluno: ')
n2 = input('Nome do 1º aluno: ')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print(f'O escolhido foi: {escolhido}.')

random.shuffle(lista)

print(f'A ordem de apresentação será: {lista}')