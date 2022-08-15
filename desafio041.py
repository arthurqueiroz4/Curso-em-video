idade = int(input('QUAL A IDADE DO COMPETIDOR? '))
if idade <= 9:
    print('COMPETIDOR MIRIM!')
elif idade <= 14:
    print('COMPETIDOR INFANTIL!')
elif idade <= 19:
    print('COMPETIDOR JUNIOR!')
elif idade <= 20:
    print('COMPETIDOR SÊNIOR!')
else:
    print('COMPETIDOR MASTER!')