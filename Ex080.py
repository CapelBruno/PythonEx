#Ex. Receba cinco números em uma lista e os ordene sem uso do sorted.

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:     #Se o c for o primeiro número ou se for maior que o maior número da lista.
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)        #Insere o número na posição certa.
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos = pos + 1
print(f'Os valores digitados em ordem foram: {lista}')