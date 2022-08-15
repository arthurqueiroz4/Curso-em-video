num = int(input('DIGITE UM NÚMERO: '))
x = 0
for n in range(1, num):
    if num % n == 0:
        x += 1
if x > 2:
    print('ESSE NÚMERO NÃO É PRIMO!')
else:
    print('ESSE NÚMERO É PRIMO!')






        #if n == 1 or n == num:
        #    print('Esse número é primo!')
        #else:
          #  print('Esse número não é primo!')