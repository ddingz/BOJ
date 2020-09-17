try:    #예외가 발생할 가능성이 있는 코드
    while True:
        a,b=map(int,input().split())
        print(a+b)
except: #예외가 발생했을 때 실행할 코드
    exit()