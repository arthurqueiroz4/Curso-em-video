total = cont = cont1 = menorp = 0
menor = ''
print('Loja de produtos')
print('-'*18)
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço : R$ '))
    total += preço
    cont += 1
    if cont == 1:
        menorp = preço
        menor = nome
    if cont != 1:
        if menorp > preço:
            menor = nome
    if preço > 1000:
        cont1 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
print(f'O produto mais barato é {menor} e custa {menorp}')
print(f'O total gasto foi {total}.')
print(f'O total de produtos que custam mais de mil reais é {cont1}.')