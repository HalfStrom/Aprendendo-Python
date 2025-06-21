# Software que ordena valores de acordo com a entrada do usuário

print("Oi, tudo bem?\nEntão eu preciso que você digite para mim alguns números inteiros para eu conseguir amazenar na minha lista.\n")

valores = []

quantidade = int(input("Quantos valores você quer colocar na lista?\n"))

print()

for i in range(quantidade):
    valor = int(input(':'))
    valores.append(valor)

print(f"\nOk, De acordo com a ordem que foi inserida a sua lista está inicialmente assim: {valores}\n")

print(" - " * 25)

def lista_crescente(valores):
    for i in range(len(valores)):
        for j in range(i+1, len(valores)):
            if valores[i] > valores[j]:
                t = valores[i]
                valores[i] = valores[j]
                valores[j] = t
    return valores

def lista_decrescente(valores):
    for i in range(len(valores)):
        for j in range(i+1, len(valores)):
            if valores[i] < valores[j]:
                t = valores[i]
                valores[i] = valores[j]
                valores[j] = t
    return valores



print(f"Lista ordenada na ordem crescente: {lista_crescente(valores)}")

print(f"Lista ordenada na ordem decrescente: {lista_decrescente(valores)}")
