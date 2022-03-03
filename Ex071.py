#Ex. Simular um caixa eletrônico. Recebe uma quantia prra sacar e distribui as notas necessárias.

valor = int(input('Digite quanto deseja sacar: R$'))
total = valor
nota = 50 #Começando com a nota mais alta.
totalnotas = 0
while True:
    if total >= nota:       #Enquanto couber o valor da nota mais alta, continue com ela.
        total = total - nota
        totalnotas = totalnotas + 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} cédulas de R${nota}')
        if nota == 50:      #Se ainda houver sobras para o restante da quantia, trata-se o valor da nota para continuar.
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnotas = 0
        if total == 0:      #Fim da necessidade de acrescentar mais notas para saque.
            break
print('Fim.')