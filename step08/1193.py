x=int(input())
n=0
while x>n:
    x-=n
    n+=1
#n이 짝수 일때 분자는 오름차순 분모는 내림차순
if n%2==0:
    print(x,'/',n-x+1,sep='')
#n이 홀수 일때 분자는 내림차순 분모는 오름차순
else:
    print(n-x+1,'/',x,sep='')