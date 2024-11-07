#def sem_rep(lista):
    #return list(set(lista)) tbm pode usar esse
def sem_rep(lista):
    numeros_semrep=[]
    repeticoes=set()
    for c in lista:
        if c not in repeticoes:
            repeticoes.add(c)
            numeros_semrep.append(c)
    return repeticoes


numeros=[1,1,2,3,4,4,8]
resultado=sem_rep(numeros)
print(resultado)