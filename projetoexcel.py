import pandas as pd
dicionario={}
geral=[]

def linha():
    return print('-'*40)



while True:
    dicionario['nome']=str(input('Nome do jogador: '))
    partidas=int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
    dicionario['gols']=[]

    for g in range(0, partidas):
        gols=int(input(f'Quantos gols na partida {g}?'))
        dicionario['gols'].append(gols)
    dicionario['total']=sum(dicionario['gols'])
    geral.append(dicionario.copy())

    while True:
        resposta=str(input('Quer continuar? [S/N]:')).upper()[0]
        if resposta in 'SN':
            linha()
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        linha()
        break
print(geral)

#cabeçalho
print('cod    ', end='')
for i in dicionario.keys():
     print(f'{i:<15}', end='')
print()
linha()
#corpo da tabela
for i, v in enumerate(geral):
    print(f'{i:<4}    {v["nome"]:<10}    {str(v["gols"]):<15}   {v["total"]:<25}') #str no gols pq é lista
print()
linha()


#colocando dados na tabela excel
salvar=str(input('Deseja salvar os dados em uma planilha do Excel [S/N]:'))
if salvar in 'Ss':
    nome_arquivo=str(input('Qual o nome do arquivo?')).strip()

    #verifica se o nome do arquivo termina com .xlsx
    if not nome_arquivo.endswith('.xlsx'):
        nome_arquivo += '.xlsx'

    df=pd.DataFrame(geral) #converte a lista em um dataframe
    df.insert(0, 'cod', pd.Series(range(len(df))))
    df.to_excel(nome_arquivo, index=False)  # Salva os dados no arquivo Excel
    print(f'Dados salvos com sucesso no arquivo {nome_arquivo}')
else:
    print('Os dados não serão salvos.')


#consulda dos jogares
while True:
    jogador=int(input('Mostrar dados de qual jogador?[999 para]:'))
    if jogador==999:
        break
    if jogador >= len(geral):
        print('ERRO! Jogador não encontrado.')
    else:
        print(f'-LEVANTAMENTO DO JOGADOR: {geral[jogador]["nome"]}') #1º [] indice 2ºvalor
        for i, g in enumerate(geral[jogador]["gols"]):
            print(f'No jogo {i} fez {g} gols')

print('volte sempre')

#999 para.
