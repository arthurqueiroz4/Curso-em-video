
aluno = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')

