print('-=-' * 20)
fala = 'MÉDIA ESCOLAR'
print('{:^60}'.format(fala))
print('-=-' * 20)
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
if ((num1 + num2) / 2) < 5:
    print('-=-' * 20)
    print('REPROVADO!')
elif ((num1 + num2) / 2) >= 5 and ((num1 + num2) / 2) <= 6.9:
    print('-=-' * 20)
    print('RECUPERAÇÃO!')
elif ((num1 + num2) / 2) >= 7:
    print('-=-' * 20)
    print('APROVADO!')
print('-=-' * 20)