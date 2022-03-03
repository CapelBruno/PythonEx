#Ex. Recolha valores numéricos enquanto o usuário desejar e os cadastre em uma lista,
#Não receba números repetidos e ao final mostre tudo em uma lista em ordem crescente.

num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Número repetido, não vou adicionar...')
    r = str(input('Quer continuar [S/N]'))
    if r in 'Nn':
        break
num.sort()
print(f'Você digitou os valores: {num}')
