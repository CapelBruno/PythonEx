peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print('Você está na categoria ABAIXO DO PESO. IMC= {:.1f} '.format(imc))
elif 18.5 < imc < 25:
    print('Você está na categoria PESO IDEAL. IMC= {:.1f} '.format(imc))
elif 25 < imc < 30:
    print('Você está na categoria SOBREPESO. IMC= {:.1f} '.format(imc))
elif 30 < imc < 40:
    print('Você está na categoria OBESIDADE. IMC= {:.1f} '.format(imc))
else:
    print('Você está na categoria OBESIDADE MÓRBIDA. IMC= {:.1f} '.format(imc))
