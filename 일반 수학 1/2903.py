# https://www.acmicpc.net/submit/2903
n = int(input())
i = 1
for _ in range(n):
    i = i * 2
    
j = 1 + i
print(j * j)