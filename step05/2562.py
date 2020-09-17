n=[]
for _ in range(9):
    n.append(int(input()))
print(max(n))
#index(x) list에 x 값이 있으면 x의 위치 값을 반환
print(n.index(max(n))+1)