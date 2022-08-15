contidade = conthomem = contmulher = 0
while True:
    idade = int(input('Digite sua idade: '))
    gen = ''
    while gen not in 'MF':
        gen = str(input('Digite seu genero: [M/F]')).upper().strip()[0]
    if idade >= 18:
        contidade += 1
    if gen == 'M':
        conthomem += 1
    if gen =='M' and idade < 20:
        contmulher += 1
    x = ''
    while x not in 'SN':
        x = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if x == 'N':
        break
print(f'O total de pessoas maiores de 18 anos é {contidade}')
print(f'O total de homens cadastrados é {conthomem}')
print(f'o total de mulheres com menos de 20 anos é {contmulher}')