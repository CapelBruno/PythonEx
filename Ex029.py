

vel = float(input('Velocidade do carro: '))
multa = (vel-80)*7

if vel>80:
    print('Você foi multado!')
    print('Sua multa é de R$ {:.2f}.'.format(multa))

else:
    print('Stay hard, stay safe!')