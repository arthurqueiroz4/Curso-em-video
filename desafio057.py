sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))