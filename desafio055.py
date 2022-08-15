maior = 0
menor = 0

'''maiorpeso = 0
menorpeso = 0'''

for i in range(1, 5):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {}'.format(maior))
print('o menor peso foi {}'.format(menor))


















'''print(f'o maior peso é {maiorpeso}')
print('o menor peso é {}'.format(menorpeso))'''