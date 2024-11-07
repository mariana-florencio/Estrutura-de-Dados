def moda(lista):
    frequencia={}
    for num in lista:
        if num in frequencia:  #se o num estiver no dict
            frequencia[num]+=1 #frequencia[num]=frequencia[num]+1
        else:
            frequencia[num]=1

    rep=[]
    for k, v in frequencia.items():
        if v>1:
            rep.append(k) # se valor for maior q 1, a chave é add na lista
    return rep


numeros=[1,1,2,3,4,4,8]
resultado=moda(numeros)
print(resultado)