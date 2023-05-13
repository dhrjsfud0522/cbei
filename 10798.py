#https://www.acmicpc.net/problem/10798

l = [input() for i in range(5)] #입력


for x in range(15):
    for y in range(5):
        try:
            print(l[y][x], end = "")
        except:
            pass