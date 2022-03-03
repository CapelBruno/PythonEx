#Ex. Crie um programa que receba nome, sexo e idade de usuários. Cada usuário terá seu dicionário
# e todos os dicionários estarão em uma lista. No final mostre quantos cadastrados houveram, qual a média de idade, uma lista apenas
#com mulheres, uma lista com idade acima da média.

pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:  #Loop de correção do sexo
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Por favor digite M ou F. ')
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    galera.append(pessoa.copy())        #Salva cada um dos usuários na lista galera.
    while True:     #Loop pra continuar adicionando usuários.
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Ditite apenas S ou N. ')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos. ')
print('As Mulhers cadastradas foram: ', end='')
print()
for p in galera:        #Pra cada pessoa na lista galera, verifica se é feminina.
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média de idade: ', end='')
for p in galera:        #Verifica quem está com mais idade que a média.
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
