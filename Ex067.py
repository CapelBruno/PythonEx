while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c} '.format(num, c, num * c))
print('Sem taboadas negativas. ')

