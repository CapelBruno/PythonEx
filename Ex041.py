ano = int(input('Digite em que ano você nasceu: '))
idade = 2022 - ano

if idade <= 9:
    print('Você pertence a categoria MIRIM. ')
elif 9 < idade < 15:
    print('Você pertence a categoria INFANTIL. ')
elif 14 < idade < 20:
    print('Você pertence a categoria JÚNIOR. ')
elif idade == 20:
    print('Você pertence a categoria SÊNIOR. ')
else:
    print('Você pertence a categoria MASTER. ')