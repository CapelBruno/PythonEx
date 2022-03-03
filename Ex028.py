import random
import time
num = random.randint(1, 5)
esc = int(input('Advinhe o número de 1 á 5: '))
print('Processando...')
sleep(3)

if num == esc:
    print('O número escolhido foi {}, parabéns você acertou!'.format(num))
else:
    print('O número escolhido foi {}, que pena você errou!'.format(num))

