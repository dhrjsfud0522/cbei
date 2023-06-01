#https://www.acmicpc.net/problem/1978

n = int(input())
x = 0
i = list(map(int, input().split()))
for k in i:
    if(k == 1):
        x += 1
    for j in range(2, int(k ** (1 / 2)) + 1):
        if(k % j == 0):
            x += 1
            break

print(n - x)