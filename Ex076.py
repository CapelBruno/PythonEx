#Ex. Crie uma listagem de produtos e seus preços usando apenas uma tupla.

listagem = ('Lápis', 1.75,      #Par\ímpar
            'Borracha', 0.50,
            'Caderno', 11.75,
            'Estojo', 18.99,
            'Mochila', 120.75,
            'Caneta', 2.75,
            'Livro', 50.00)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:        #Condição para verificar se é o produto (pares)
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)