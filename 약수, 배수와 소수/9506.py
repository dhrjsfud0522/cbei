#https://www.acmicpc.net/problem/9506

while True:
        n = int(input())
        if( n == -1):
             break
        a = 0
        l = []
        for i in range(1, n):
            if (n % i == 0):
                l.append(i)
                a += i
        if(n == a):
            print(n, "=", end = " ")
            print(*l, sep = " + ")
        else:
            print(n, "is NOT perfect.")