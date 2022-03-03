num = int(input('Dgite um número inteiro: '))
escolha = int(input('Escolha a base para conversão, Binário(1), Octal(2), Hexadecimal(3). '))

if escolha == 1:
    print('O número {} convertido para BINÁRIO é: {}'.format(num, bin(num)[2:])) #bin(num[2:]))) bin é a conversão e 2: é o fatiamento da string de resposta
elif escolha == 2:
        print('O número {} convertido para OCTAL é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
        print('O número {} convertido para HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
        print('Opção inválida, tente novamente.')