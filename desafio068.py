from random import randint

cont = 0
while True:
    pc = randint(0, 9)
    n = int(input('Digite um número:'))
    parimpar = str(input('Você quer par (P) ou impar (I)?')).upper()
    if parimpar == 'P':
        if (n + pc) % 2 == 0:
            print(f'O computador escolheu {pc} e vc escolheu {n}, a soma desses é {n + pc} que é um número par. Vc ganhou!')
            cont += 1
        else:
            print(f'O computador escolheu {pc} e vc escolheu {n}, a soma desses é {n + pc} que é um número impar. Vc perdeu!')
            print(f'Vc ganhou {cont} vezes!')
            break
    if parimpar == 'I':
        if (n + pc) % 2 == 1:
            print(f'O computador escolheu {pc} e vc escolheu {n}, a soma desses é {n + pc} que é um número impar. Vc ganhou!')
            cont += 1
        else:
            print(f'O computador escolheu {pc} e vc escolheu {n}, a soma desses é {n + pc} que é um número par. Vc perdeu!')
            print(f'Vc ganhou {cont} vezes!')
            break
