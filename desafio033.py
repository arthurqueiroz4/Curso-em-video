a = int(input('Digite um numero '))
b = int(input('Digite outro numero '))
c = int(input('Digite outro numero '))

if a > b and a > c:
    print('O maior número é: {}'.format(a))
if b > a and b > c:
    print('O maior número é: {}'.format(b))
if c > a and c > b:
    print('O maior número é {}'.format(c))

if a < b and a < c:
    print('O menor número é {}'.format(a))
if b < a and b < c:
    print ('O menor numero é {}'.format(b))
if c < a and c < b:
    print('O menor numero é {}'.format(c))