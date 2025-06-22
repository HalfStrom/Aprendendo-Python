# Lanche

codigo, qtd = map(int, input().split())

itens = (40, 45, 50, 20, 15)

if 1 <= codigo <= len(itens):
    total = itens[codigo - 1] * qtd
    print(f"Total: R$ {total/10:.2f}")
else:
    print("Código inválido!")