L1=[]
L2=[]
L3=[]

tamanho1=int(input('TAMANHO LISTA 1:'))
for c in range(1,tamanho1+1):
    n1=int(input(f'{c}º valor:'))
    if n1 not in L1:
        L1.append(n1)

tamanho2=int(input('TAMANHO LISTA 2:'))
for d in range(1,tamanho2+1):
    n2=int(input(f'{d}º valor:'))
    if n2 not in L1:
        L2.append(n2)

L3=L1+L2
L3.sort()

decrescente=sorted(L3, reverse=True)
print(f'L3 ordenada crescente{L3}')
print(f'L3 ordenada decrescente: {decrescente}')
