#Ex. Crie um programa que leia nome e peso de usuários e mostre quantos cadastros e quais os mais pesados e mais leves.

temp = []         #Lista temporária para cadastro.
princ = []      #Lista principal.
mai = men = 0

while True:                                             #Lista [0, 1] == [nome, peso]
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float('Digite seu peso: '))
    if len(princ) == 0:                             #Caso seja o primeiro cadastro.
        mai = men = temp[1]                     #O primeiro peso é o maior e o menor, posteriormente serve para comparação.
    else:
        if temp[1] > mai:           #Definindo comparações e classificando maior e menor pesos.
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])       #Cria uma cópia de toda a lista temporária.
    temp.clear()                #Limpa a lista temporária.
    resp = str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
print(f'Ao todo você cadastrou{len(princ)} pessoas. ')      #Tudo que está na lista principal.
print(f'O maior peso foi de{mai}Kg. Peso de: ')
for p in princ:                             #Pra cada item na lista principal verificar se o peso é o maior.
    if p[1] == mai:
        print(f'{p[0]}', end='')
for p in princ:                             #Pra cada item na lista principal verificar se o peso é o menor.
    if p[1] == men:
        print(f'{p[0]}', end='')