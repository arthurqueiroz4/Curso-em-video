print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇO'))
print('-'*40)
produtos = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

cont = 0
print('-'*40)
while True:

    print('{:.<30}R$ {:.2f}'.format(produtos[cont], produtos[cont + 1]))
    cont += 2
    if cont > 17:
        break
print('-'*40)