#Ex. Estatísticas em produtos, receba produtos e valores enquanto o usuário desejar e ao final escreva o valor total da compra,
# quantos produtos custam mais de mil reais e qual o produto mais barato.

total = caro = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont = cont + 1
    total = total + preço
    if preço >= 1000:       #Definindo quantos produtos custam mais de mil reias.
        caro = caro + 1
    if cont == 1 or preço < menor:    #Setando o valor inicial das variáveis menor e barato para comparações no loop.
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é R${total:.2f}. ')
print(f'São {caro} produtos que custam mais de R$1000.00 ')
print(f'O produto mais barato custa R${menor:.2f}. ')
print('Fim.')