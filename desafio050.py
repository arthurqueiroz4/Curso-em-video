soma = 0
for i in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os pares digitados é {}'.format(soma))