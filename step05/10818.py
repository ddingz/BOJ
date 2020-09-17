n=int(input())
#list(map(int,input().split())) map으로 나눠서 list형식으로 저장
n_list=list(map(int,input().split()))
print(min(n_list),max(n_list))