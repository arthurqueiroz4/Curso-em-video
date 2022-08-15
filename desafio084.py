lista = []
lista1 = []
peso = []
mai = men = 0
while True:
    lista1.append(input('Nome: '))
    lista1.append(input('Peso: '))
    if len(lista) == 0:
        mai = men = lista1[1]
    else:
        if lista1[1] > mai:
            mai = lista1[1]
        if lista1[1] < men:
            men = lista1[1]
    lista.append(lista1[:])
    lista1.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-' * 20)
print(f'O total de pessoas cadastradas foi {len(lista)}.')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for i in lista:
    if i[1] == mai:
        print(f'{i[0]},', end='')
print(f'\nO menor peso foi de {men}. Peso de ', end='')
for i in lista:
    if i[1] == men:
        print(f'{i[0]},', end='')

