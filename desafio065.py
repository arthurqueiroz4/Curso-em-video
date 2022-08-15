resp = str('S')
maior = float()
menor = float()
somador = int()
cont = int(0)
num = int()
while resp == 'S':
    num = int(input('Digite um número: '))
    somador = somador + num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += +1
    resp = str(input('Vc deseja continuar? [S/N]')).upper()
m = somador / cont
print(somador)
print(cont)
print('a média entre esses numeros foi '.format(m))
print('o maior numero digitado foi {}'.format(maior))
print('o menor numero digitado foi {}'.format(menor))