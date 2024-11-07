def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f


def combinacao(M, N):
    c=fatorial(M)/(fatorial(M-N) * fatorial(N))
    return c


m=int(input('Valor de M:'))
n=int(input('Valor de N:'))
resultado=combinacao(m,n)
print(f'O Resultado é: {resultado}')