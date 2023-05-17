# https://www.acmicpc.net/problem/10988

l = list(input())
i = 1
k = 0
for n in range(0, len(l) // 2):
    if(l[n] != l[len(l) - n - 1]):
        i = 0
        k += 1

print(i)