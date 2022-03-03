import random

itens = ('Pedra', 'Papel', 'Tesoura')
comp = random.randint(0, 2)

escolha = int(input('Escolha Pedra(0), Papel(1) ou Tesoura(2): '))
if escolha < 3:
    print('O Computador escolheu {}. '.format(itens[comp]))
    print('Você escolheu {}. '.format(itens[escolha]))


if comp == 0:
    if escolha == 0:
        print('Empate! ')
    elif escolha == 1:
        print('Jogador vence.')
    elif escolha == 2:
        print('Computador vence')
    else:
        print('Jogada inválida.')
elif comp == 1:
    if escolha == 0:
        print('Computador vence. ')
    elif escolha == 1:
        print('Empate!')
    elif escolha == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida.')
elif comp == 2:
    if escolha == 0:
        print('Jogador Vence ')
    elif escolha == 1:
        print('Computador vence.')
    elif escolha == 2:
        print('Empate!')
    else:
        print('Jogada inválida.')
else:
    print('Jogada inválida.')


