#Ex. Colha informações sobre uma variável com funções 'is***'

n = input('Digite algo:')        #Atribuição de variável.

print('O tipo primitivo dessa entrada é:', type(n))     #Info sobre a variável ser str(palavra) int(inteiro) float(flutuante).

print(n.isalnum())      #Funções 'is***' nos dão indicação do que a entrada é.
print('A entrada é alnumérico?', n.isalpha())       #Se a variável é alfabética.
print('A entrada pertence a tabela ASCII?', n.isascii())        #Se a variável pertence a tabela ASCII.
print('A entrada é numeral?', n.isdigit())      #Se a variável é um dígito.
print('A entrada está em minúsculas?', n.islower())     #Se a variável está toda em letras minúsculas.
print('A entrada é decimal?', n.isdecimal())        #Se a variável é um número decimal.
print('Essa é a verão capitalizada da entrada:', n.capitalize())        #Se a primeira letra da variável é maiúscula.
print('A entrada é imprimível?', n.isprintable())       #Se a variável é imprimível.
print('A entrada é feita de espaços?', n.isspace())     #Se a variável é um espaço.
print('A entrada está em caixa alta?', n.isupper())     #Se a variável está toda com letras maiúsculas.
