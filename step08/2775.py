for _ in range(int(input())):
    k=int(input())
    n=int(input())
    apart=[i for i in range(1,n+1)] #[1,2,3,...,n]
    for _ in range(k):  #k층만큼 반복
        for i in range(1,n):
            #앞의 원소를 더하면서 그 위층의 사람 수를 구함
            apart[i]+=apart[i-1]
    print(apart[-1])