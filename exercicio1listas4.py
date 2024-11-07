L=[]
tamanho=int(input('Tamanho da lista:'))
for c in range(1,tamanho+1):
    num=int(input(f'Digite seu {c}º número:'))
    if num not in L:
        L.append(num)

for num in L:
    if num % 2==0:
        L.remove(num)
print(L)