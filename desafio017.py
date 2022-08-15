import math
catop = float(input('Valor do cateto oposto: '))
catad = float(input('Valor do cateto adjascente: '))
hip = math.sqrt(pow(catop, 2) + pow(catad, 2))
print('Valor da hipotenusa: {:.0f}'.format(hip))