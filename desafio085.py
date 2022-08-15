num = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Valores pares: {num[0]}')
print(f'Valores ímpares: {num[1]}')
