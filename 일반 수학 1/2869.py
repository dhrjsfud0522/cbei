#https://www.acmicpc.net/problem/2869

a, b, v = list(map(int, input().split()))
v -= a
v = v + a - b - 0.5

print(int(v // (a - b) + 1))