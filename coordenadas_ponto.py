# Coordenadas de um Ponto

x, y = map(float, input().split())

if x == y == 0:
    print("Origem")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")