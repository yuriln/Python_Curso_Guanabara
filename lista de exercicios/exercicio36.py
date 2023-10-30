try:
    vl_cs = float(input('Qual o valor da casa? '))
    vl_sal = float(input('Qual o seu salario?'))
    tp_pag = int(input('Em quantos anos você irá pagar? '))

    parcelas = tp_pag * 12
    vl_parc = vl_cs / parcelas

    print(f'O valor da parcela será {vl_parc:.1f}')
  
    if  vl_parc <= vl_sal * 0.3:
        print('O valor do seu financianciamento foi aprovado')
    else:
        print('Seu salário não permite o financiamento.')
except ValueError:
    print('Insira um valor correto')