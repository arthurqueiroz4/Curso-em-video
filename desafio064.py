n = int(0)
cont = int(0)
somador = int(0)
while n != 999:
    n = int(input('Digite um número (digite 999 para parar o programa).'))
    print(n)
    cont += 1
    somador = somador + n
print('a quantidade de numeros digitados foram: {}'.format(cont - 1))
print('a soma desses números foram: {}'.format(somador - 999))