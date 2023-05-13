#https://www.acmicpc.net/problem/2563

ll = [[0 for _ in range(101)]for _ in range(101)]

for _ in range(int(input())):
    x, y = list(map(int,input().split()))
    for i in range(10):
        ll[y + i][x:x+10] = [1] * 10

m = 0
for a in range(101):
    for b in range(101):
        if ll[a][b] == 1:
            m = m + 1

print(ll)
