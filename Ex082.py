#Ex. Crie um programa que recolha números em uma lista e depois os separe em uma lista de pares e uma de ímpares.

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):     #Enumera os itens da lista num.
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')