lista = []

while True:
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Quer continar? [S/N]'))
    if resp in 'Nn':
        break
listapar = []
listaimpar = []
for x in lista:
    if x % 2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)

print(f'a lista completa é {lista}'
      f'\na lista somente de pares é {listapar}'
      f'\na lista somente de impares é {listaimpar}')