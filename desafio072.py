cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
'dezenove', 'vinte')
n = int(input('Digite um número: '))
while n > 21 or n < 0:
    n = int(input('Digite um número novamente: '))
print(cont[n])