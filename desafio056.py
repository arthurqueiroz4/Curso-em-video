idade = 0
idadeH = 0
totalidade = 0
menos20 = 0
maisvelho = ''

for i in range(1, 5):
    print('------{}° PESSOA------'.format(i))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('1 -> masculino \n2-> feminino \n'))

    #somatorio da idade
    totalidade += idade

    #maior idade homem
    if sexo == 1:
        if i == 1:
            if idade > idadeH:
                idadeH = idade
                maisvelho = nome
        else:
            idadeH = idade
            maisvelho = nome
    #mulher menos de 20
    if sexo == 2:
        if idade < 20:
            menos20 += 1

#media da idade
print('-' * 20)
mediaidade = totalidade / (i + 1)
print('a média das idades é {}.'.format(mediaidade))

#homem mais velho
print('o nome do homem mais velho homem é {}.'.format(maisvelho))

#mulher menos de 20
print('existem {} mulheres com menos de 20 anos.'.format(menos20))