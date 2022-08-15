from random import randint
from time import sleep
megasena = []
jogos = []
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
rep = int(input('Quantos jogos quer que eu sorteie? '))
print('-=' * 3, f' Soteando {rep} jogos', '=-' * 3)
for c in range(0, rep):
        #Gerador de numeros
        for i in range(0, 6):
            var = randint(1, 60)
            while not megasena.count(var) == 0:
                var = randint(1, 60)
            megasena.append(var)
        #
        megasena.sort()
        jogos.append(megasena[:])
        megasena.clear()
        print(f'Jogo {c + 1}: {jogos[c]}')
        sleep(1)
