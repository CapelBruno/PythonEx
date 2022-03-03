#Ex. Crie um programa que guarde os dados de um jogador de futebol e os mostre ao final. Nome, número de partidas,
#gols em cada uma delas e o total de gols marcados.

jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range (1, tot+1):        #Contador que usa o total de partidas jogadas.
    partidas.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['Gols'] = partidas[:]       #Copia todos os dados de gols e os salva em um espaço apenas.
jogador['Total'] = sum(partidas)        #Soma todos os gols colocados nas partidas.
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'   O campo {k} tem o valor {v}. ')
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas. ')   #len jogador gols é o tamanho da lista que define as partidas.
for i, v in enumerate(jogador['Gols']):     #Enumera cada um dos items em gols
    print(f'  Na partida {i+1}, fez {v} gols. ')
print(f'Foi um total de {jogador["Total"]} gols. ')