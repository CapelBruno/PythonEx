#Ex. Crie um programa que pegue quatro valores de entrada e guarde-os em uma tupla,
#depois mostre quantas vezes apareceu o 9, que posição houve o primeiro 3 e quais números foram pares.

num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Você colocou os valores: {num}. ')
print(f'O número 9 apareceu {num.count(9)} vezes. ')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1} posição. ')
else:
    print('O número 3 não foi digitado. ')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


