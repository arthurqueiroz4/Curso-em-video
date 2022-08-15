import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = random.choice(lista)
num2 = int(input('Digite um número: '))
cont = 1
while num1 != num2:
    num2 = int(input('Digite um número novamente: '))
    cont += 1

print('Parabéns, vc acertou em {} tentativas!'.format(cont))