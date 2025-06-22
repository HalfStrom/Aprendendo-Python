# Média 3

N1, N2, N3, N4 = map(float, input().split())

pesos = (2, 3, 4, 1)

N1 *= pesos[0]
N2 *= pesos[1]
N3 *= pesos[2]
N4 *= pesos[3]

media = (N1 + N2 + N3 + N4) / (sum(pesos))

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media >= 5 and media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    exame = (nota_exame + media) / 2
    if exame >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {exame:.1f}")
else:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")