#https://www.acmicpc.net/problem/2444

n = int(input())
i = 1
a = 2 * n - 1
for _ in range(a):
    print(" " * ((a - i) / 2), end = "")
    print("*" * i)
    i = i + 2

    
