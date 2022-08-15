cont = s =  0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O total de números digitados foi {cont} e a soma foi {s}')