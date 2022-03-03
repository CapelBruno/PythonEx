r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos FORMAM triângulo.')

    if r1 == r2 == r3:
        print('O triângulo é equilátero. ')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é Escaleno. ')
    else:
        print('O triângulo é Isóceles. ')

else:
    print('Os segmentos NÃO FORMAM triângulo.')
