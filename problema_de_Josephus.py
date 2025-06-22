def josephus(n, k):
    res = 0
    for i in range(2, n+1):
        res = (res + k) % i
    return res + 1

NC = int(input())
for caso in range(1, NC + 1):
    n, k = map(int, input().split())
    vencedor = josephus(n, k)
    print(f"Case {caso}: {vencedor}")