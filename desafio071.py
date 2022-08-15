valor = int(input('Qual o valor que vc quer sacar?'))
ced50 = (valor // 50)
print(f'Vc vai receber {ced50} cedulas de 50')
ced20 = (valor - (ced50 * 50)) // 20
print(f'Vc vai receber {ced20} cedulas de 20.')
ced10 = ((valor - (ced50 * 50)) - (ced20 * 20)) // 10
print(f'Vc vai receber {ced10} cedulas de 10.')
ced1 = (((valor - (ced50 * 50)) - (ced20 * 20)) - (ced10 * 10)) // 1
print(f'Vc vai receber {ced1} cedulas de 1.')