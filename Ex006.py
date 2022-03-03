#Ex. Escreva o dobro, o triplo e a raiz quadrada de uma variável.

n = int(input('Digite um número:\n'))
dob = n*2
tri = n*3
raiz = n**(1/2)     #Manobra matemática da raiz quadrada.
print(' O dobro é: {}\n O triplo é: {}\n A raiz quadrada é: {:.2f}'.format(dob, tri, raiz))     #{:.2f} pega 2 casas a partir da vígula.