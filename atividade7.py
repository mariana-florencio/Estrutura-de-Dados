valorsaque=int(input('Valor do saque: R$ '))
if valorsaque<10 or valorsaque>1500:
    print('Erro: O valor do saque deve ser entre R$ 10 e R$ 1500.')
else:
    print('-'*40)
    for nota in [200, 100, 50, 20, 10, 5, 1]:
        quantidade=valorsaque//nota
        valorsaque=valorsaque%nota
        if quantidade>0:
            print(f'{quantidade} notas de R$ {nota}')
