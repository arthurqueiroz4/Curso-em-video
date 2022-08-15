from random import randint

print('-=-' * 4)
print('   JOKENPÔ')
print('-=-' * 4)
jgdr1 = int(input('1 -> pedra \n2 -> papel \n3 -> tesoura \nResponda: '))
pd = 'pedra'
pp = 'papel'
t = 'tesoura'
lista = (pd, pp, t)
computador = randint(0,2)
print('O computador escolheu: {}.'.format(lista[computador]))
#1 - PEDRA
#2 - PAPEL
#3 TESOURA
if jgdr1 == 1 and computador == 0:
    print('EMPATE!')
elif jgdr1 == 1 and computador == 1:
    print('COMPUTADOR GANHOU!')
elif jgdr1 == 1 and computador == 3:
    print('VOCÊ GANHOU!')

elif jgdr1 == 2 and computador == 0:
    print('VOCÊ GANHOU!')
elif jgdr1 == 2 and computador == 1:
    print('EMPATE!')
elif jgdr1 == 2 and computador == 3:
    print('COMPUTADOR GANHOU!')

elif jgdr1 == 3 and computador == 0:
    print('COMPUTADOR GANHOU!')
elif jgdr1 == 3 and computador == 1:
    print('VOCÊ GANHOU!')
elif jgdr1 == 3 and computador == 3:
    print('EMPATE!')

