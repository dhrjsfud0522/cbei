#https://www.acmicpc.net/problem/4344

c = int(input())
for _ in range(c):
    k = list(map(int, input().split()))
    n = k[0]
    k.remove(n)
    p = sum(k) / n
    i = 0
    for l in k:
        if(l > p):
            i += 1
    print(f'{(i / n * 100):.3f}', '%', sep = '')