# https://www.acmicpc.net/problem/2720

for _ in range(int(input())):
    j = 0
    k = 0
    l = 0
    h = 0
    n = int(input())
    j, n = int(n // 25), (n - int((n // 25) * 25))
    k, n = int(n // 10), (n - int((n // 10) * 10))
    l, n = int(n // 5), (n - int((n // 5) * 5))
    h, n = int(n // 1), (n - int((n // 1) * 1))
    print(j, k , l, h)