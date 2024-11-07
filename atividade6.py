peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura:'))
imc=peso/(altura)**2
if imc <=18.5:
    print('Você está abeixo do peso.')
elif 18.5<= imc <= 25:
    print('Você está com o peso adequado')
elif 25 <= imc <= 30:
    print('Você está acima do peso.')
else:
    print('Você está obeso!')