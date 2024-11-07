n=int(input('Quantos pokemons deseja cadastrar?'))
d={}
maior_ataque=0
nome_maisF=''

for i in range(n):
    nome=str(input('NOME:'))
    tipo=str(input('TIPO:')).lower()
    ataque=int(input('ATAQUE:'))
    print('=-'*20)
    if tipo=='fogo':
        d[nome]=[tipo, ataque]
    if (tipo=='fogo' and ataque>maior_ataque):
        maior_ataque=ataque
        nome_maisF=nome

if nome_maisF:
    print(f'O POKEMON DO TIPO FOGO COM MAIOR ATAQUE É:{nome_maisF}.')
else:
    print('Nenhum pokemon do tipo FOGO foi encontrado.')
