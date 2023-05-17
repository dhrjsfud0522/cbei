#https://www.acmicpc.net/problem/1934
import math
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    print(math.lcm(n,m))
#    on, om = n, m
#    while True:
#        n, m = m, n% m
#
#        if(m == 0):
#            break
#    print(on * om//n)

#유클리드 형 폼 미쳤다