d = float(input('Qual a distância da viagem? '))
curta = 0.50 * d
longa = 0.45 * d
if d <= 200:
    print('A viagem é curta. O valor a pagar é de R$ {:.2f}.'.format(curta))
else:
    print('A viagem é longa. O valor a pagar é de R$ {:.2f}.'.format(longa))
