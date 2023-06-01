#https://www.acmicpc.net/problem/2581

m = int(input())
a = int(input())
i = 0
sum = 0
min = a
for n in range(m, a + 1):
    x = 0
    for _ in range(1):
        if(n == 1):
            x = 1
            break
        for j in range(2, int(n** (1 / 2)) + 1):
            if(n != j):
                if(n % j == 0):
                    x += 1
                    break
    if(x == 0):
        sum += n
        if(n < min):
            min = n
        i += 1

if(i == 0): print(-1)
else: 
    print(sum)
    print(min)