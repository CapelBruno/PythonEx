#Ex. Crie um programa que receba sete valores numéricos em uma lista única,
#separe-os em pares e ímpares e no fim os mostre em ordem crescente.

num = [[], []]          #Declarando uma lista com duas listas dentro.
valor = 0
for c in range(1, 8):        #Cadastro dos sete números.
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 ==0:       #Se for par.
        num[0].append(valor)                #Coloque na primeira lista dentro da lista completa.
    else:                   #Se for ímpar.
        num[1].append(valor)                #Coloque na segunda lista dentro da lista completa.
num[0].sort()   #Organizando em ordem crescente
num[1].sort()
print(f'Os números pares digitados foram: {num[0]}. ')
print(f'Os números ímpares digitados foram: {num[1]}. ')
