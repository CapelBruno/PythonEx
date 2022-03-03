#Ex. Escreva o número digitado como entrada por extenso, usando tuplas.
#Tuplas são imutáveis.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('Digite um valor: '))
    if 0 <= valor <= 20:        #Filtro evitando erro de digitação do valor pelo usuário.
        break
print(f'Você digitou o número: {extenso[valor]}.')
