n=int(input())
cycle=n
cnt=0
while True:
    #(cycle%10)*10 일의 자리 숫자를 십의 자리로
    #(cycle//10+cycle%10)%10 십의 자리 숫자와 일의 자리 숫자 합의 일의 자리 숫자
    cycle=(cycle%10)*10+(cycle//10+cycle%10)%10
    cnt+=1
    if cycle==n:
        break
print(cnt)