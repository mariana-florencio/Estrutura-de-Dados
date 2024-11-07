from math import gcd
from functools import reduce
def mdc_2(lista):
    return reduce(gcd, lista)


numeros=[]
quant=int(input('Quantos números deseja por na lista:'))
for c in range(quant):
  numero =int(input(f'Digite o {c+1}º número:'))
  numeros.append(numero)

resultado_mdc=mdc_2(numeros)
print('-='*30)
print(f'Lista de números: {numeros}')
print(f'MDC: {resultado_mdc}')