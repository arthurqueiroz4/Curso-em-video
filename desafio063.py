print('SEQUÊNCIA FIBONACCI: ')
x = 0
y = 1
n = int(input('Quantos termos da sequência vc quer ver?'))
cont: int = int(2)
print('0 \n1')
while cont < n:
    z = x + y
    print(z)
    x = y
    y = z

    cont += 1
