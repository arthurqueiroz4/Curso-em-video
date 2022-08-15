expressao = str(input('Digite uma expressão: '))
expressao1 = ' '.join(expressao)
lista = [expressao1.split()]
cont = 0

for x in lista:
      if x == '(' or x == ')':
            cont += 1
print(cont)
if cont % 2 == 0:
      print('Sua expressão está correta.')
else:
      print('Sua expressão está incorreta.')
