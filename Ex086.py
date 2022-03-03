#Ex. Crie um programa que receba valores e mostre uma matriz 3x3 ao final.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]      #Criando três listas para a matriz
for l in range(0, 3):       #Pra cada linha no intervalo 3.
    for c in range(0, 3):   #Pra cada coluna no intervalo 3.
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')       #^5 centraliza em cinco espaços 00n00
        print()     #Quebra uma linha a cada loop