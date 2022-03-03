#Ex. Crie um programa que verifique se uma expressão matemátima está corretamente parametrizada com parêntesis.

expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == ('('):       #Verifica se há um parêntesis no início.
        pilha.append('(')
    elif simb == (')'):     #Senão verifica se há um parêntesis no final
        if len(pilha) > 0:
            pilha.pop()     #Apaga o último elemento da lista.
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida. ')
else:
    print('Sua expressão é inválida. ')