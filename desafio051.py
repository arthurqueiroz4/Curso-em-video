a1 = float(input('Digite o primeiro termo da P.A.: '))
r = float(input('Digite a razão dessa P.A.: '))
n = 1
#an = a1 + (n - 1) * r
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an)