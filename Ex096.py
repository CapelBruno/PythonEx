#Ex. Use função para um programa que calcule área de um terreno retangular.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}X{comp} é {a}m². ')


#Programa principal
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)