import random
lista = [0, 1, 2, 3, 4, 5]
num1 = random.choice(lista)
num2 = int(input('Digite um número: '))
if num2 == num1:
    print('Parabéns, vc acertou o numero!')
else:
    print('Vc errou, tente outra vez.')