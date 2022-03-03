idade = cont = maior = masc = fem = 0

while True:
    idade = int(input('Digite sua idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:     #Se menor de idade
        maior = maior + 1
    if sex == 'M':
        masc = masc + 1
    if sex == 'F' and idade < 20:
        fem = fem + 1
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).strip().upper()
    if novo == 'N':
            break
print(f'Houveram {maior} pessoas maiores de idade: ')
print(f'Foram {masc} homens cadastrados: ')
print(f'Foram {fem} mulheres cadastradas com menos de 20 anos: ')
