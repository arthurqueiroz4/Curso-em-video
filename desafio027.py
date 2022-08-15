name = str(input('Digite seu nome completo: ')).strip()
div = name.split()
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))

