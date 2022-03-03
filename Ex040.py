n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média é {:.1f}'.format(n1, n2, media))

if media < 5:
    print('Você foi reprovado. ')
elif 4.9 < media < 7:
    print('Você está de recuperação. ')
else:
    print('Você foi aprovado. ')
