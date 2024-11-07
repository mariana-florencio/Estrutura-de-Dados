def diferenca(a,b):
    dif=[]
    for num in a:
        if num not in b:
            dif.append(num)
    return dif


conjuntoa=[1,2,3,4]
conjuntob=[3,4,5,6] #a-b=1,2 ------5  Elementos de A que não estão em B.
resultado=diferenca(conjuntoa,conjuntob)
print(resultado)