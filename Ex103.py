#Ex. Crie um programa com uma função ficha() que receba dois parâmetros opcionais, o nome de um jogador e quantos gols ele marcou.
#O programa deve mostrar uma ficha mesmo que algum dado não tenha sido informado corretamente

def ficha(jog = '<desconhecido>', gol = 0 ):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato. ')


#Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip == '':
    ficha(gol=g)
else:
    ficha(n, g)
    