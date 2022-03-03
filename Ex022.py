#frase = 'Curso em Vídeo Python'
#print(frase[13:])
#
#print("""Quando quiser escrever textos longos, use três aspas""")
#
#print(len(frase.strip()))  #len de lenght(comprimento) #strip remove espaços antes e dps da frase
#a = frase.replace('Python', 'Android')      #replace troca uma palavra por outra
#print(a)
#dividido = frase.split()
#print(dividido)

frase = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: {}'.format(frase.upper()))
print('Seu nome em maiúsculas é: {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(frase) - frase.count(' ')))
dividido = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras.' .format(dividido[0], len(dividido[0])))




