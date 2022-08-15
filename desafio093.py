partida = {}
num_gols = []
partida['nome'] = str(input('Nome do jogador: '))
num_partidas = int(input('Número de partidas: '))
partida['total'] = 0
for i in range(0, num_partidas):
    gols = int(input(f'Quantos gols na partida {i}: '))
    num_gols.append(gols)

partida['gols'] = num_gols
partida['total'] = sum(num_gols)


print('-=' * 30)

for k, v in partida.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)

print(f'O jogador {partida["nome"]} jogou {num_partidas} partidas.')
for i in range(0, num_partidas):
    print(f'    => Na partida {i}, fez {partida["gols"][i]} gols.')
print(f'Foi um total de {partida["total"]}.')


