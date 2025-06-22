# Carrega ou não Carrega?
"""
while True:
    try:
        linha = input()
        if linha.strip() == "":
            continue
        a, b = map(int, linha.strip().split())
        print(a ^ b)
    except EOpyFError:
        break
"""

import sys

for line in sys.stdin:
    if not line.strip():
        continue
    a, b = map(int, line.strip().split())
    print(a ^ b)