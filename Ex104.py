#Ex. Crie um programa que tenha a função leiaInt(), que funcione similar a função input(), só que só aceite um valor numérico.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))     #Recebe a entrada.
        if n.isnumeric():       #Se for numeral.
            valor = int(n)      #Classifica como inteiro.
            ok = True   #Validação.
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:      #Se a msg for um número,quebra do loop.
            break
    return valor


#Programa principal

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}. ')
