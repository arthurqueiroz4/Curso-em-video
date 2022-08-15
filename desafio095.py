partida = {}
num_gols = []
time = []
while True:
    partida.clear()
    partida['nome'] = str(input('Nome do jogador: '))
    num_partidas = int(input('Número de partidas: '))
    partida['total'] = 0
    num_gols.clear()
    for i in range(0, num_partidas):
        num_gols.append(int(input(f'Quantos gols na partida {i}: ')))
    partida['gols'] = num_gols[:]
    partida['total'] = sum(num_gols)
    time.append(partida.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod ', end='')
for k in partida.keys():
    print(f'{k:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-'*40)