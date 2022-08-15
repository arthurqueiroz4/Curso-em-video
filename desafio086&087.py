matriz = []
l = c = i = pares = maior = 0

while True:
    matriz.append(int(input(f'Digite um valor para [{c},{l}]: ')))
    if matriz[i] % 2 == 0:
        pares += matriz[i]
    i += 1
    if l == 2 and c == 2:
        break
    l += 1
    if l > 2:
        c += 1
        l = 0
print('-=' * 30)
print('[',matriz[0],']','[', matriz[1],']','[', matriz[2],']', end='\n')
print('[', matriz[3],']','[', matriz[4],']','[', matriz[5],']', end='\n')
print('[', matriz[6],']','[', matriz[7],']','[', matriz[8],']', end='\n')
print('-=' * 30)
print(f'a) Soma dos pares = {pares}')
soma3coluna = matriz[2] + matriz[5] + matriz[8]
print(f'b) Soma dos valores da terceira coluna = {soma3coluna}')
if matriz[3] >= matriz[4] and matriz[3] >= matriz[5]:
    maior = matriz[3]
if matriz[4] >= matriz[3] and matriz[4] >= matriz[5]:
    maior = matriz[4]
if matriz[5] >= matriz[4] and matriz[5] >= matriz[3]:
    maior = matriz[5]
print(f'c) Maior valor da segunda linha = {maior}')
