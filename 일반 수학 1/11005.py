#https://www.acmicpc.net/problem/11005

n, b = input().split()
n = int(n)
b = int(b)
l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(65, 91):
    l.append(chr(i))

a = []
while(n >= b):
    a.append(n % b)
    n = n // b
a.append(n)


for i in range(1, len(a) + 1):
    print(l[a[len(a) - i]], end = '')
