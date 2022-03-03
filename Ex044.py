pn = float(input('Qual o preço do produto? '))
pag = int(input('O pagamento será feito em:\n 1.Dinheiro\n 2.Cartão\n 3.Cheque\n '))

if pag == 1 or pag == 3:
    desc = (pn / 100) * 10
    pf = pn - desc
    print('Você ganhou um desconto de 10%, o valor á pagar é: {:.2f} '.format(pf))
elif pag == 2:
    parcelas = int(input('Você deseja parcelar em quantas vezes? '))
    if parcelas <= 2:
        print('O valor á pagar é de R$ {:.2f}'.format(pn))
    else:
        juros = (pn / 100) * 20
        pfp = pn + juros
        print('O valor á pagar é de R$ {:.2f}'.format(pfp))



