num1 = int(input('DIGITE UM NUMERO: '))
num2 = int(input('DIGITE OUTRO NUMERO: '))
if num1 > num2:
    print('O {} é maior que o {}.'.format(num1, num2))
elif num1 < num2:
    print('o {} é maior que o {}.'.format(num2, num1))
else:
    print('Nao existe valor maior,pois, {} e {} são iguais.'.format(num1, num2))