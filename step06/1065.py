def han(n):
    cnt=0
    for i in range(1,n+1):
        #한 자릿수, 두 자릿수는 모두 한수
        if i<100:
            cnt+=1
        #세 자릿수는 첫 번째와 두 번째 숫자, 두 번째와 세 번째 숫자의 차가 같을 경우 한수
        else:
            nl=list(map(int,str(i)))
            if nl[0]-nl[1]==nl[1]-nl[2]:
                cnt+=1
    return cnt
n=int(input())
print(han(n))