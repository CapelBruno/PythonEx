casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos levará para pagá-la? '))

limiteprest = (salario / 100) * 30
numprest = anos * 12
valorprest = casa / numprest

if valorprest <= limiteprest:
    print('Parabéns, seu empréstimo foi aprovado. ')
    print('O valor das prestações será de R$ {:.2f}. '.format(valorprest))
else:
    print('Sinto muito, seu empréstimo foi negado.')
