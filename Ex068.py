import random

cont = soma = 0
escolha = ' '

while True:
    jog = int(input('Jogue seu número: '))
    comp = random.randint(0, 10)
    soma = jog + comp
    while escolha not in 'PI':
        escolha = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()
    print(f'Você escolheu {jog} e o computador escolheu {comp}, a soma é igual á {soma}')
    if soma % 2 == 0:
        if escolha == 'P':
            cont = cont + 1
            print('Parabéns, você ganhou! ')
        else:
            break
    if soma % 2 == 1:
        if escolha == 'I':
            cont = cont + 1
            print('Parabéns, você ganhou! ')
        else:
            break
print (f'Você perdeu. Você Teve {cont} vitórias consecutivas. ')
