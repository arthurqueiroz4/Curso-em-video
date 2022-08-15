lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append((input('Digite um número: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if maior < lista[i]:
            maior = lista[i]
        if menor > lista[i]:
            menor = lista[i]
print(f'O maior valor digitado foi {maior} nas posições ', end= '')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end= '')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
