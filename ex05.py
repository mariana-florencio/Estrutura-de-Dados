def fatores(a):
    fatoresprimos=[]
    divisor=2
    while a >1:
        while a % divisor == 0:
            fatoresprimos.append(divisor) # adiciona o divisor para a lista
            a/=divisor #a=a//d
        divisor+=1
    return fatoresprimos


n=int(input('Digite um numero inteiro para ver seus fatores primos:'))
resultado=fatores(n)
print(f'Fatores:{resultado}')