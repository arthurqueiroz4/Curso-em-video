r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da segunda reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo.')
    if r1 == r2 == r3:
        print('TRIÂNGULO EQUILÁTERO!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('TRIÂNGULO ISÓCELES!')
    else:
        print('TRIÂNGULO ESCALENO!')
else:
    print('IMPOSSÍVEL FAZER UM TRÂNGULO COM ESSAS RETAS.')