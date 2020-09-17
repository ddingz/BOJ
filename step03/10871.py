n,x=map(int,input().split())
#list(map(int,input().split())) map으로 나눠서 list형식으로 저장
a=list(map(int,input().split()))
for i in a:  
    if i<x:
        print(i,end=' ')