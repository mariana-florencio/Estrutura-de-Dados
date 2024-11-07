def mmc(a, b):
    if a == 0 or b == 0:
        return 0  # O MMC de qualquer número com 0 é 0
    maior = max(a,b)
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1


n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
print(f"O MMC de {n1} e {n2} é {mmc(n1, n2)}")
