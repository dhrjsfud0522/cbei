#https://www.acmicpc.net/problem/1085

l = list(map(int, input().split()))
n = [l[0], l[1], l[2] - l[0], l[3] - l[1]]
i = sum(n)

for j in n:
    if(i > j):
        i = j
        
print(i)