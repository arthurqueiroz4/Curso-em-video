import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('SEN = {:.3f} ; COS = {:.3f} ; TG = {:.3f}.'.format(sen, cos, tg))