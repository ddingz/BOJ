n=int(input())
#list(map(int,input().split())) map으로 나눠서 list형식으로 저장
score=list(map(int,input().split()))
score=[i/max(score)*100 for i in score]
print(sum(score)/n)