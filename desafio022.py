name = str(input('Digite seu nome completo: '))
print(name.upper())
print(name.lower())

space = name.count(' ')
namenospace = len(name) - space
print('O total de letras sem o espaço é {}.'.format(namenospace))

div = name.split()
print('Número total de letras no primeiro nome é {}'.format(len(div[0])))
