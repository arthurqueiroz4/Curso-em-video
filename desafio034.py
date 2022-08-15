salario = float(input('Qual o valor do salario '))
if salario > 1250:
    salario = salario * 1.10
    print(salario)
else:
    salario = salario * 1.15
    print(salario)