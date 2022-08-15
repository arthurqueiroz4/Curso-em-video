from datetime import datetime
geral = {}
geral['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
geral['idade'] = datetime.now().year - nasc
geral['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if geral['ctps']  != 0:
    geral['contratação'] = int(input('Ano de contratação: '))
    geral['salário'] = float(input('Salário: '))
    if geral['idade'] - geral['contratação'] < 35:
        geral['aposentadoria'] = 35 - (nasc - geral['contratação'])

for k, v in geral.items():
    print(f'{k} tem o valor {v}')

