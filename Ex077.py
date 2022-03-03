#Ex. Crie uma tupla com várias palavras e identifique as vogais em cada uma delas.

palavras = 'Aprender', 'Viver', 'Python', 'Corinthians', 'Music'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')
