#Ex. Crie uma conversão de R$ para U$.

n = float(input('Digite o valor em reais:\n'))
d = 3.27                                                #Cotação do dollar
conv = n/d
print('O valor em U$ é: {}'.format(conv))
