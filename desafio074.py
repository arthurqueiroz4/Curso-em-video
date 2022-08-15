import random
cont = 0
n1 = n2 = n3 = n4 = n5 = 0
while True:
    num = int(random.randint(0, 9))

    if cont == 0:
        n1 = num
    if cont == 1:
        n2 = num
    if cont == 2:
        n3 = num
    if cont == 3:
        n4 = num
    if cont == 4:
        n5 = num
    if cont == 5:
        break
    cont += 1
total = n1, n2, n3, n4, n5
print(total)
print(sorted(total))
print(f'O maior número é {sorted(total)[4]}')
print(f'O menor número é {sorted(total)[0]}')