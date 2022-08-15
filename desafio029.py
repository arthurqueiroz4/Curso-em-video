veloc = float(input('Digite a velocidade do carro: '))
if veloc >= 80:
    multa = veloc - 80
    valor = multa * 7
    print('Voce foi multado em {}'.format(valor))

    