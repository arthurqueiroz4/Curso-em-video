preconormal = float(input('Digite o preço normal do produto: '))
forma = int(input(' 1 -> À vista.\n 2 -> À vista no cartão. \n 3 -> 2x no cartão. \n 4 -> 3x ou mais no cartão.\n Responda: '))
avista = preconormal * 0.9
avistacartao = preconormal * 0.95
doisxcartao = preconormal
tresxcartao = preconormal * 1.2

if forma == 1:
    print('O novo preço será de {} reais.'.format(avista))
elif forma == 2:
    print('O novo preço será de {} reais.'.format(avistacartao))
elif forma == 3:
    print('O novo preço será de {} reais.'.format(doisxcartao))
elif forma == 4:
    print('O novo preço será de {} reais.'.format(tresxcartao))