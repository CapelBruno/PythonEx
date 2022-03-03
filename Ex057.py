sex = str(input('Digite o seu sexo [M\F]: ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Dados inválidos, por favor digite seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso! '.format(sex))
