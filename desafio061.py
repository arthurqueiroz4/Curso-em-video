a1 = float(input('Digite o primeiro termo da P.A.: '))
r = float(input('Digite a razão dessa P.A.: '))
n = 1
cont = 0
#an = a1 + (n - 1) * r
while n < 11:
    an = a1 + (n - 1) * r
    print(an)
    n += 1
#n = 10
novo = int(input(('vc quer ver mais quantos termos?')))
n1 = novo + n
while n < n1:
    an = a1 + (n - 1) * r
    print(an)
    n += 1
