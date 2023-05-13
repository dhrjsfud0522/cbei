#https://www.acmicpc.net/problem/2444

n = int(input())
i = -1
a = 2 * n - 1
for _ in range(n):
    i = i + 2
    print(" " * ((a - i) // 2), end = "")
    print("*" * i)
for _ in range(n - 1):
    i = i - 2 
    print(" " * ((a - i) // 2), end = "")
    print("*" * i)
      