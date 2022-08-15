dist = float(input('Digite a distância da viagem: '))
if dist >= 200:
    valor = dist * 0.45
    print('O valor da viagem será {}.'.format(valor))
else:
    valor = dist * 0.5
    print('O valor da viagem será {}.'.format(valor))