v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2 and v1 != v2:
    print('O primeiro valor é maior. ')
elif v1 == v2:
    print('Não existe valor maior, os dois são iguais. ')
else:
    print('O segundo valor é maior. ')
