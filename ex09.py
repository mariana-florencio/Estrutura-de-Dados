def uniao(l1,l2):
    conjuntouniao=l1+l2
    conjuntouniao.sort()
    return list(set(conjuntouniao)) #converte o conjunto para lista


lista1=[1,2,3,4,5]
lista2=[10,9,5,8,2]
resultado=uniao(lista1,lista2)
print(resultado)