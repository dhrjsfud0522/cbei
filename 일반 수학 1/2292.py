#https://www.acmicpc.net/problem/2292

n = int(input())

j = 1

for i in range(1, 1000000000):

    j += (6 * (i - 1))
    
    if(n <= j):
        print(i)
        break