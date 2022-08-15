menu = int(0)
result = 0
num1 = int(input('Digite o primeiro valor '))
num2 = int(input('Digite o segundo valor '))

while menu != 5:
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    menu = int(input('Digite o que vc deseja que o computador execute:'))
    print(menu)
    if menu == 1:
        resul = num1 + num2
        print('a somar é {}'.format(resul))
    if menu == 2:
        resul = num1 * num2
        print('a multiplicação é {}'.format(resul))
    if menu == 3:
        if num1 > num2:
                print('{} é maior que {}.'.format(num1, num2))
        if num1 < num2:
                print('{} é maior que {}.'.format(num2, num1))
    if menu == 4:
            print('Quais novos números vc quer colocar?')
            num1 = input('1° numero =')
            num2 = input('2° numero =')
