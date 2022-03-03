num = soma = cont = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'Foram digitados {cont} números e a soma deles é = {soma}')
