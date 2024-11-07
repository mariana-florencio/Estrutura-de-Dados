from math import gcd
from functools import reduce

def mmc(a, b):
    return abs(a * b) // gcd(a, b)


def mmc_2(lista):
    return reduce(mmc, lista)


numeros = []
quant = int(input('Quantos números deseja por na lista: '))
for c in range(quant):
    numero = int(input(f'Digite o {c + 1}º número: '))
    numeros.append(numero)

resultado_mmc = mmc_2(numeros)

print('-=' * 25)
print(f'Lista de números: {numeros}')
print(f'MMC: {resultado_mmc}')
