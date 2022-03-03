#Ex. Crie um programa que receba nome e duas notas de alunos e os guarde em uma lista. No final mostre um boletim com os nomes
#e a média dos alunos e permita que possam ser acessadas as notas individuais de um aluno.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])     #Adiciona todos os dados á uma lista composta.
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME:<10"}{"MÉDIA":>8}')
for i, a in enumerate(ficha):      #Listagem de cada índice na lista de alunos.
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:       #Mostra a posição 2 da lista ficha = [nome, notas, media]
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')