frase = str(input('Digite uma frase: ')).strip()
maiusc = frase.upper()
cont = maiusc.count('A')
print('O numero de vezes que A apareceu foi {}.'.format(cont))
print('A primeira letra A foi encontrada na posição {}'.format(maiusc.find('A') + 1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1))
