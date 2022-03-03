#Ex. Crie um programa com uma função voto(), que recebe o ano de nascimento e retorna se a pessoa precisa votar obrigatóriamente,
#Se ela ainda não vota ou se o voto é opcional.

def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: Não vota. ')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: Voto opcional. ')
    else:
        print(f'Com {idade} anos: Voto obrigatório. ')


#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))