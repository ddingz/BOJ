n=int(input())
cnt=-1
#5킬로그램 봉지 개수를 점점 커지게 하여 최소 개수를 구함
for i in range(n//5+1):
    for j in range(n//3+1):
        if 5*i+3*j==n:
            cnt=i+j
print(cnt)