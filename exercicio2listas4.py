p1=[]
p2=[]

tamanho=int(input('Tamanho da turma:'))
for c in range(1,tamanho+1):
    notas1=float(input(f'{c}º nota P1:'))
    if notas1 not in p1:
        p1.append(notas1)

print('-='*20)

for d in range(1,tamanho+1):
    notas2=float(input(f'{d}º nota P2:'))
    if notas2 not in p2:
        p2.append(notas2)

mediap1=sum(p1)/len(p1)
mediap2=sum(p2)/len(p2)
print(f'MÉDIA DA TURMA NA PROVA 1: {mediap1:.2f}')
print(f'MÉDIA DA TURMA NA PROVA 2: {mediap2:.2f}')
if mediap1> mediap2:
     print('A turma obteve a maior média na prova 1')
else:
     print('A turma obteve a maior média na prova 2')