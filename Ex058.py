import random

print('Olá, vou pensar em um número de 0 á 10, tente acertar! ')
num = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador > num:
        print('Menos... tente outra vez!')
    elif jogador < num:
        print('Mais... tente outra vez')
    else:
        acertou = True
        print('Você acertou, foram necessárias {} tentativas!'.format(palpites))


