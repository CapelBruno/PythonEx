#Ex. Crie um programa que tenha uma função notas() e guarde um dicionário com:
#Quantidade de notas, maior nota menor nota, média da turma e a situação.

def notas(* n, sit=False):
    """
    -->Função que analisa notas e situação de alunos.
    :param n: uma ou mais notas
    :param sit: opcional, indica se é para mostrar ou não a situação.
    :return: Dicionário com várias informações sobre a turma.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] =  'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
