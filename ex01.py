def mdc(a,b):
    while b != 0:
        a, b = b, a % b #troca os valoress
    return a


n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
print(f' O MDC de {n1} e {n2} é {mdc(n1,n2)}')

