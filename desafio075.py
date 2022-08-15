nums = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'Voce digitou os valores {nums}')
print(f'O valor 9 foi digitado {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O valor 3 apareceu na posição {nums.index(3)}°.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ',end='')
for n in nums:
    if n % 2== 0:
        print(n, end=' ')