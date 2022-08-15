lista = []
cont = 0

while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'Nn':
        break

print(lista)
print('=' * 20)
print(f'Foram digitados {len(lista)} números')
print('=' * 20)
lista.sort(reverse=True)
print(f'A lista em ordem decrescente foi {lista}')
print('=' * 20)
lista.count(5)
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')

print('=' * 20)