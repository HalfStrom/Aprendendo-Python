# Notas e Moedas

notas = (10000, 5000, 2000, 1000, 500, 200)
moedas = (100, 50, 25, 10, 5, 1)

N = float(input())
centavos = round(N * 100)

print("NOTAS:")
for nota in notas:
    qtd = centavos // nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
    centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    qtd = centavos // moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")
    centavos %= moeda
