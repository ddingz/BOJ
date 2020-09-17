for _ in range(int(input())):
    score=list(map(int,input().split()))
    avg=sum(score[1:])/score[0]
    n=0
    for i in score[1:]:
        if i>avg:
            n+=1
    #{:.3f} 소수점 3번째 자리까지 출력
    print('{:.3f}%'.format((n/score[0])*100))