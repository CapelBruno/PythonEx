frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece por último na posição {}.'.format(frase.rfind('A')+1))