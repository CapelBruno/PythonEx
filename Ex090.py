#Ex. Crie um dicionário que leia o nome e a média de um aluno e mostre sua situação (Aprovado ou reprovado).

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():      #Pra cada key e value no dicionário aluno
    print(f' {k} é igual a {v}')