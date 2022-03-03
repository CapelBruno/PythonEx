import datetime

ano = int(input('Digite em que ano você nasceu: '))
atual = datetime.date.today().year
idade = atual - ano

if idade == 18:
    print('Já está na hora de se alistar. ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não chegou a hora de se alistar, faltam {} anos. '.format(saldo))
else:
    saldo = idade - 18
    print('Você devia ter se alistado há {} anos. '.format(saldo))
