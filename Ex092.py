#Ex. Crie um programa que receba nome, ano de nascimento e registro da carteira de trabalho de usuários em um dicionário,
#junto com o ano de contratação e o salário. Calcule a idade e também com quantos anos a pessoa vai se aposentar.

import datetime

dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.datetime.now().year - nasc            #Ano atual - ano de nascimento
dados['CTPS'] = int(input('Carteira de trabalho [0 se não tiver]: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.datetime.now().year)  #Idade+(idade da aposentadoria-ano atual)
for k, v in dados.items():      #Pra cada Key e value no dicionário dados
    print(f'{k} tem o valor {v}')