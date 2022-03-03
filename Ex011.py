#Ex. Calcule a área de uma parede e quantas latas de tinta serão necessárias para pintá-la, sabendo que cada lata pint 2m² de parede.

lar = float(input('Digite a largura da parede:\n'))
alt = float(input('Digite a altura da parede:\n'))
a = lar*alt
t = 2
qnt = a/t
print('A quantidade de tinta necessária é: {}'.format(qnt))