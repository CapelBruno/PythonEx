#Ex. Crie um programa com uma função contador() que recebe como parâmetro início, fim e passo.
#Realize as contagens de 1 até 10 de 1 em 1, de 10 até 0 de 1 em 1 e uma contagem personalizada.
import time

def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    time.sleep(2.5)     #Aguarda pro usuário ler a mensagem de cima
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)   #flush atualiza
            time.sleep(0.5)
            cont = cont + p
        print('Fim.')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont = cont - p
        print('Fim.')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize a contagem.')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)