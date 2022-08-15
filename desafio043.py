peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (pow(altura, 2))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA!')
