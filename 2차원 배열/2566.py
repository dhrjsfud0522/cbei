#https://www.acmicpc.net/problem/2566

l = []
xl = []
mx = 0 #최대값 열
my = 0 #최대값 행
for i in range(9): #9번 반복
    xl = list(map(int, input().split())) #한줄 입력 받기
    l.append(xl) #전체 리스트에 추가하기
    for n in xl: 
        if(n > l[my][mx]): #만약 현재 최대값보다 새로 입력 받은게 크다면
            my = i #현재 열
            mx = xl.index(n) #현재 행

print(l[my][mx])
print(my+1, mx+1)