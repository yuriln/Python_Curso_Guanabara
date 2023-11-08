numero = int(input('Digite um número inteiro: '))

binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)
try:
    print("Opção 1: converte em binário")
    print("Opção 2: converte em octal")
    print("Opção 3: converte em hexadecimal")

    opcao = int(input('Escolha uma opção: '))
 
    if opcao == 1 :
        print(f'Binário igual a: {binario}')
    elif opcao == 2:
        print(f'Octal igual a: {octal}')
    elif opcao == 3:
        print(f'Hexadecimal igual a: {hexa}')
    else:print('Digite uma das opções listadas.')

except ValueError: print('Digite um valor valido')