#https://www.acmicpc.net/problem/5073

while(True):
    try:
        a, b, c = list(map(int, input()))

        if(a == b == c):
            print("Equilateral")
        if(a == b != c or a != b == c or a == c != b):
            print("Isosceles")
        if(a != b != c):
            print("Scalene")
        else:
            print("Invalid")
    except:
        break