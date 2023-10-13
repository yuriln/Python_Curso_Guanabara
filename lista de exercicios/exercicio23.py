num = input('Insira um número de 0 a 9999: ')

# Verifica se a entrada é um número inteiro
if num.isdigit():
    num = int(num)

    # Verifica se o número está na faixa permitida
    if 0 <= num <= 9999:
        num_str = str(num)

        # Preenche zeros à esquerda se necessário
        num_str = num_str.zfill(4)

        # Extrai e imprime as unidades, dezenas, centenas e milhares
        print(f'Milhar: {num_str[0]}')
        print(f'Centena: {num_str[1]}')
        print(f'Dezena: {num_str[2]}')
        print(f'Unidade: {num_str[3]}')
    else:
        print('Número fora da faixa permitida (0 a 9999)')
else:
    print('Por favor, insira um número válido.')
