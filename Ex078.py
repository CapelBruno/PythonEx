#Ex. Crie um programa que leia 5 valores e coloque-os em uma lista, no final mostre o maior e menor e onde estão na lista

listanum = []
mai = men = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))        #.append adiciona um valor de entrada á lista.
    if c == 0:      #Setando que o primeiro valor será o maior e também o menor.
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:       #Durante o loop vai comparando cada novo valor e atribuindo qual é o maior e o menor.
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os valores {listanum} ')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):        #Numera a lista e a compara com o valor maior, i salva as posições onde o valor aparece.
    if v == mai:
        print(f'{i}, ')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):        #Numera a lista e a compara com o valor menor, i salva as posições onde o valor aparece.
    if v == men:
        print(f'{i}, ')
print()