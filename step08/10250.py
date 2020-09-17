for _ in range(int(input())):
    h,w,n=map(int,input().split())
    #n%h는 층을 결정
    floor=n%h
    #n//h+1은 호수를 결정
    room=n//h+1
    #n%h가 0일 때 꼭대기 층의 n//h호수를 가짐
    if floor==0:
        floor=h
        room-=1
    print(floor*100+room)