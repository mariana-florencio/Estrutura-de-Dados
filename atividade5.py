comprimento=float(input('Digite o comprimento do terreno:'))
largura=float(input('Digite a largura do terreno:'))
areatotal=comprimento*largura
iptu=areatotal*8.14
print(f'O valor do seu IPTU será de R${iptu:.2f}')