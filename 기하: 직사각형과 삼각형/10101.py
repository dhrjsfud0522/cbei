#https://www.acmicpc.net/problem/10101

a = int(input())
b = int(input())
c = int(input())

if((a + b + c) != 180):
    print("Error")
elif(a == b == c == 60):
    print("Equilateral")
elif(a == b != c or a != b == c or a == c != b):
    print("Isosceles")
elif(a != b != c):
    print("Scalene")