print('-'*10)
print(' TABUADAS')
print('-'*10)
while True:
    n = int(input('Digite um número:'))
    if n < 0:
        print('Programa encerrado.')
        break
    else:
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')