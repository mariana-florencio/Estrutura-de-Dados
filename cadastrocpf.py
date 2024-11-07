lista=[]
cpfsrepeticoes=set()
n=int(input('Deseja cadastrar quantas pessoas?'))
for c in range(1,n+1):
    nome=str(input('NOME:'))
    cpf=str(input('CPF:'))
    idade=int(input('IDADE:'))
    print('-='*25)
#ou tbm podemos usar: (nome, cpf, idade)=input().split()
                       #idade= int(idade) PARA DIGITAR TUDO E UMA SO LINHA

    if cpf not in cpfsrepeticoes:
        cpfsrepeticoes.add(cpf)
        lista.append({'nome':nome, 'cpf': cpf, 'idade':idade}) #lista vai receber um dict

for p in lista:
    print(f'NOME:{p["nome"]}, CPF:{p["cpf"]}, IDADE:{p["idade"]}')
