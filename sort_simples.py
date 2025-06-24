# Sort Simples
# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os
# valores em ordem crescente, um linha em branco e em seguida, os valores na
# sequência como foram lidos.

n1, n2, n3 = map(int, input().split())

valores_ordenados = sorted([n1, n2, n3])

for valor in valores_ordenados:
    print(valor)

print()

print(n1)
print(n2)
print(n3)
