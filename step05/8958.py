for _ in range(int(input())):
    ox=input()
    cnt=0
    o=ox.split('X')
    for i in o:
        #가우스의 덧셈(1부터 n까지의 합) n*(n+1)/2
        cnt+=len(i)*(len(i)+1)//2
    print(cnt)