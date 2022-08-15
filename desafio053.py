frase = str(input('Digite uma frase: ')).strip().upper()
contrario = frase[::-1]
contrario1 = contrario.split()
contrario2 = ''.join(contrario1)
separa = frase.split()
junta = ''.join(separa)
print(junta)
print(contrario2)
if junta == contrario2:
    print('Temos um palíndromo.')
else:
    print('Não temos um palídromo.')

