larg = float(input('Qual a largura em metros da parede? '))
alt = float(input('Qual a altura em metros da parede? '))
area = larg * alt
tint = 2
lts = area / tint
print('Você usará um total de {} litros de tinta.'.format(lts))