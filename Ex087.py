#Ex. Melhore o ex anterior colocando a soma dos valores pares na matriz, a soma dos elementos da terceira linha
# e o maior valor da segunda coluna.

spar = mai = scol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]      #Criando três listas para a matriz
for l in range(0, 3):       #Pra cada linha no intervalo 3.
    for c in range(0, 3):   #Pra cada coluna no intervalo 3.
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')       #^5 centraliza em cinco espaços 00n00.
        if matriz[l][c] % 2 == 0:       #Se o valor dor par, acumula na variável spar.
            spar = spar + matriz[l][c]
        print()     #Quebra uma linha a cada loop.
print(f'A soma dos valores pares é: {spar}. ')
for l in range(0, 3):
    scol = spar + matriz[l][2]      #Adiciona a soma da coluna(sempre a [2] da lista).
print(f'A soma dos valores da terceira coluna é: {spar}. ')
for c in range(0, 3):
    if c == 0:      #Compara pra definir o maior (sempre a linha 1).
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}. ')
