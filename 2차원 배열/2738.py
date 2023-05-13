# https://www.acmicpc.net/problem/2738

ll = []
rl = []

n, m = list(map(int, input().split()))
#n개의 줄의 m개의 원소

for _ in range(n): #좌항 입력
    t = list(map(int, input().split()))
    ll.append(t)


for l in ll:
    r = list(map(int , input().split()))
    for i in zip(l, r):
        print(sum(i), end = " ")
    print()