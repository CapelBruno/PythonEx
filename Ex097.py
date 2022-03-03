#Ex. Crie um prgrama com uma função escreva(), que mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa principal
escreva('Bruno Capel')
escreva('Futebol')
escreva('O Palmeiras não tem mundial!')
