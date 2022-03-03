import random

nums = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os números sorteados foram: ', end='')
for n in nums:
    print(f'{n} ', end='')
print(f'\n O maior número sorteado foi: {max(nums)}')
print(f'\n O menor número sorteado foi: {min(nums)}')