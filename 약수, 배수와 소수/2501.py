#https://www.acmicpc.net/problem/2501

n, m = list(map(int, input().split()))
l = 0
k = 0
for i in range(1,n + 1):
    if(n % i == 0):
      l = i
      k += 1
    if(k == m):
       break

if ( k == m):
   print(l)
else:
   print(0)