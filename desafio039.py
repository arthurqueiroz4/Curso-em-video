idade = int(input('QUAL A SUA IDADE: '))
antes = 18 - idade
depois = idade - 18
if idade < 18:
    print('Ainda nao está na hora de vc se alistar, faltam {} ano(s) para vc se alistar.'.format(antes))
elif idade == 18:
    print('Está na hora de vc se alistar.')
elif idade > 18:
    print('Já passou em {} ano(s) o tempo de vc se alistar.'.format(depois))