#https://www.acmicpc.net/problem/5073

while(True):
        a, b, c = list(map(int, input().split()))
        if(a == b == c == 0):
            break
        max = a
        if(max < b):
            max = b
        if(max < c):
            max = c
        if((a + b + c - max) <= max):
            print("Invalid")
        
        elif(a == b == c):
            print("Equilateral")
        elif(a == b or b == c or a == c):
            print("Isosceles")
        elif(a != b != c):
            print("Scalene")