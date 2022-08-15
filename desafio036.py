valorcasa = float(input('DIGITE O VALOR DA CASA: '))
salcomp = float(input('DIGITE O VALOR DO SEU SALÁRIO: '))
tempo = int(input('EM QUANTOS ANOS IRÁ QUITAR O EMPRÉSTIMO: '))
print('-=-' * 20)
mensal = valorcasa / (tempo * 12)
print('O VALOR DA PARCELA SERÁ {}'.format(mensal))
lim = bool(mensal <= (salcomp * 0.3))
print('VC PODERÁ PAGAR? TRUE OR FALSE?{}'.format(lim))
if mensal >= (salcomp * 0.3):
    print('VC NÃO PODE FAZER O EMPRÉSTIMO PARA COMPRAR A CASA!')
else:
    print('VC PODE FAZER O EMPRÉSTIMO PARA COMPRAR A CASA!')