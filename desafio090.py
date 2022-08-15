escola = {}
escola['nome'] = str(input('Nome: '))
escola['media'] = float(input(f'Média de {escola["nome"]}: '))
print(f'Nome é igual a {escola["nome"]}')
print(f'Média é igual a {escola["media"]}')
if escola["media"] > 7:
    escola["situação"] = 'Aprovado'
else:
    escola["situação"] = 'Reprovado'
print(f'Situação é igual {escola["situação"]}')