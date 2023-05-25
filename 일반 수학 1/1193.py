n = int(input())
k = 0 #끝 번호
h = 0 #최대 숫자, 개수
for i in range(1, 10000000):
    h += 1
    k += i
    if(k >= n):
        break

j = k- (i - 1) #첫 번호
a = h - (n - j)
b = 1 + (n - j)
if(h % 2 == 0):
    a, b = b, a
print(a, b, sep = '/')
