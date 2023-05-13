#https://www.acmicpc.net/problem/3003

l = list(map(int, input().split()))

n = [1, 1, 2, 2, 2, 8]
g = [0] * 6
for i in range(0, 6):
    g[i] = n[i] - l[i]

print(*g)
