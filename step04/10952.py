while True:
    a,b=map(int,input().split())
    if a==0 and b==0:   #0 0을 입력받았을 때 반복문 종료
        break
    print(a+b)