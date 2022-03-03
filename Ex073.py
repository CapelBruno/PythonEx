#Ex. Crie uma tupla com 20 times do Brasileirão e mostre os 5 primeiros colocados, 4 últimos colocados,
# ordem alfabética e onde a chapecoense está posicionada.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sort',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Tabela Brasileirão: {times}\n')
print(f'Cinco primeiros: {times[:5]}\n')
print(f'Quatro últimos: {times[-4:]}\n')
print(f'Ordem alfabética {sorted(times)}\n')        #Sorted deixa tudo organizado em ordem alfabética.
print(f'A posição da chapecoense é a {times.index("Chapecoense")+1}. ')