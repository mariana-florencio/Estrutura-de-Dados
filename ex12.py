def subconjunto(l1,l2):
    verifica=True
    for num in l1:
        if num not in l2:
            verifica=False
        else:
            verifica=True
    return verifica


conjuntoa=[2, 4]
conjuntob=[1, 2, 3, 4, 5]
resultado=subconjunto(conjuntoa,conjuntob)
print(resultado)
