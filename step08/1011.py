'''
1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 . . .(거리가 1씩 늘어날 때 최솟값)
거리가 n^2-n+1이상 n^2이하 일 때 n*2-1을 최솟값으로 가짐
거리가 n^2+1이상 n^2+n이하 일 때 n*2를 최솟값으로 가짐
'''
for _ in range(int(input())):
    x,y=map(int,input().split())
    d=y-x
    cnt=1
    while True:
        #** 거듭제곱
        if cnt**2-cnt+1<=d<=cnt**2+cnt:
            break
        cnt+=1
    print(cnt*2-1 if d<=cnt**2 else cnt*2)