def intersecao(a,b):
    uniao=[]
    uniao=a+b
    todos=[]
    inter=[]
    for num in uniao:
        if num not in todos:
            todos.append(num)
        else:
            inter.append(num)
    return list(set(inter))


conjuntoa=[1,1,2,3,4]
conjuntob=[1,3,9,8]
resultado=intersecao(conjuntoa,conjuntob)
print(resultado)