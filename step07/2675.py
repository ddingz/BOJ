for _ in range(int(input())):
    r,s=input().split()
    p=''
    #문자를 순서대로 반복 횟수만큼 늘림
    for i in s:
        p+=i*int(r)
    print(p)