#Ex. Crie um programa que crie jogos da mega sena para o usuário.

import random

jogo = []
listacompleta = []
cont = 0
quant = int(input('Quantos jogos você quer sortear? '))     #Quantidade de jogos que o usuário deseja.
tot = 1
while tot <= quant:         #Enquanto o tota for menor o igual ao valor da quantidade de jogos solicitados.
    cont = 0
    while True:
        num = random.randint(1, 60)     #Sorteia um número entre 1 e 60.
        if num not in jogo:
            jogo.append(num)
            cont = cont + 1
        if cont >= 6:
                break
    jogo.sort()         #Organiza os números do jogo.
    listacompleta.append(jogo[:])           #Copia toda a combinação de números do loop e os salva em uma outra lista.
    jogo.clear()        #Limpa a lista jogo.
    tot = tot + 1
print(f'Sorteando {quant} jogos. ')
for i, l in enumerate(listacompleta):       #Pra cada um dos índices na lista completa.
    print(f'Jogo {i+1}: {l}')

