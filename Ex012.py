n = float(input('Digite o valor do produto:\n '))
desc = (n/100)*5
vf = n-desc
print('O valor com desconto de 5% é: R${:.2f}.'.format(vf))