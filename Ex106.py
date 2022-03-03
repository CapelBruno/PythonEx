#Ex. Faça um mini-sistema que sirva como manual de um comando e quando o usuário digita "Fim" o programa se encerra
import time
c = ('\033[m',          #Sem Cores
     '\033[0;30;41m',    #1 Vermelho
     '\033[0;30;42m',    #2 Verde
     '\033[0;30;43m',    #3 Amarelo
     '\033[0;30;44m',    #4 Azul
     '\033[0;30;45m',    #5 Roxo
     '\033[7;30m'       #6 Branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print (c[6], end='')
    help(com)
    print(c[6], end='')
    time.sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    time.sleep(1)


#Programa principal
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo', 1)