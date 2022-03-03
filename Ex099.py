#Ex. Crie um programa com uma função maior() que compare e escreva qual o maior valor recebido.
import time
def maior(* num):
    cont = maior = 0
    print('\n Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        time.sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f'\nForam informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')


#Programa principal
maior(2, 9 ,5, 7, 1)
maior(0, 2 ,4)
maior(6, 4 ,7)
maior(0, 5)