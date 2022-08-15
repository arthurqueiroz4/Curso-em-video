lista = list()
while True:
    n = int(input('Digite um valor: '))
    if (n in lista) == False:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    x = str(input('Quer continuar? [S/N]')).upper().strip()
    if x == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')