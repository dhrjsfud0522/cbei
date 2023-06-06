#https://www.acmicpc.net/problem/2745

l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(65, 91):
    l.append(chr(i))

n, b = input().split()
b = int(b)
n = list(n)

k = len(n) - 1
x = 0
for j in range(0, len(n)):
    x += b ** k * l.index(n[j])
    k -= 1

print(x)