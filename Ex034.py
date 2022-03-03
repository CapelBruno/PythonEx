salario = float(input('Qual é seu salário atual? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} agora vai receber R$ {:.2f}'.format(salario, novo))