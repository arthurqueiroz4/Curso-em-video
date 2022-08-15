cadastro = {}
lista = []
cont = somatorio = 0
while True:
    cadastro['nome'] = (input('Nome: '))
    while True:
        cadastro['sexo'] = (input('Sexo: [M/F] ')).upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    somatorio += cadastro['idade']
    lista.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    cont += 1
    cadastro.clear()
    if resp in 'N':
        break
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média da idade é de {somatorio / cont:.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end=' ')
print(f'Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= (somatorio / cont):
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')

            print()
print('<< ENCERRADO >>')