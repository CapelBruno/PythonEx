#Ex. Reescreva a função leiaInt() do Ex 104, incluindo a possibilidade de digitação de um número inválido. Crie também um leiaFloat().

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2:.2f}')