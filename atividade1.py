idade=int(input('Digite sua idade:'))
if idade < 0 or idade > 150:
    print('IDADE INVÁLIDA.')
if idade <= 10:
    print('Classificação: CRIANÇA')
elif idade <=13:
    print('CLASSIFICAÇÃO: PRÉ ADOLESCENTE')
elif idade <= 17:
    print('CLASSIFICAÇÃO: ADOLESCENTE')
elif 18<= idade <= 150:
    print('CLASSIFICAÇÃO: MAIOR DE IDADE.')