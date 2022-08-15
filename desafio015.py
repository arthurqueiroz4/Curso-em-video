km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias se passaram? '))
pkm = km * 0.15
pdias = dias * 60
total = pkm + pdias
print('Com {}km percorridos, paga-se {} reais. E com {} dias, paga-se {} reais.'.format(km, pkm, dias, pdias))
print('Portanto, o total fica {} reais.'.format(total))
