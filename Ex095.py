#Ex. Melhore o Ex 93, inclua a possibilidade de cadastrar mais jogadores e também um sistema pra visualizar o aproveitamento.

jogador = {}
partidas = []
time = []

while True:
    jogador.clear()     #Limpa dados antes de um novo loop
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()    #Limpa dados antes de um novo loop
    for c in range (1, tot+1):        #Contador que usa o total de partidas jogadas.
        partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
    jogador['Gols'] = partidas[:]       #Copia todos os dados de gols e os salva em um espaço apenas.
    jogador['Total'] = sum(partidas)        #Soma todos os gols colocados nas partidas.
    time.append(jogador.copy())
    while True:     #Loop pra continuar adicionando usuários.
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Ditite apenas S ou N. ')
    if resp == 'N':
        break
for i in jogador.keys():
    print(f'{i} ')
for k, v in enumerate(time):
    print(f'{k} ')
    for d in v.values():
        print(f'{str(d)} ')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não existe nenhum jogador com código {busca}! ')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f' No jogo {i+1} fez {g} gols. ')