#Ex. Crie um programa que tenha uma lista com números e duas funções sorteia(0 e somapar()
#A primeira sorteia 5 números e a segunda soma todos os que forem pares.

import random
import time


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        time.sleep(0.3)
    print('Pronto.')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista} temos {soma} ')

numeros = []
sorteia(numeros)
somapar(numeros)

