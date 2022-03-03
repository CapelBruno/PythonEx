n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
option = 0
while option != 5:
    print('''    [1]Soma
    [2]Multiplica
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    option = int(input('Qual a sua opção? '))
    if option == 1:
        r = n1 + n2
        print('A Soma é {}. '.format(r))
    elif option == 2:
        r = n1 * n2
        print('A Multiplicação é {}. '.format(r))
    elif option == 3:
        if n1 < n2:
            print('{} é maior que {}. '.format(n2, n1))
        else:
            print('{} é maior que {}'.format(n1, n2))
    elif option == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    if option == 5:
        print('Finalizando... ')
print('Fim. ')