nummaiores = 0
nummenores = 0
for i in range(1, 8):
    idade = int(input('Qual sua idade? '))
    if idade >= 21:
        nummaiores += 1
    else:
        nummenores += 1
print('o número de maiores é {}'.format(nummaiores))
print('O número de menores é {}'.format(nummenores))

