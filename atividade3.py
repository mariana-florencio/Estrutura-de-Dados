total=0
for n in range(1,7):
    nota=float(input(f'Digite a nota {n}:'))
    total+=nota
media=total/6
print(f'Sua média é : {media}')
if media < 4.5:
    print('Reprovado.')
elif 4.5<=media<=6:
    print('Você terá que fazer a prova substitutiva.')
else:
    print('Parabéns. APROVADO!')