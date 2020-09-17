n=[]
for _ in range(10):
    n.append(int(input())%42)
#set 중복된 값을 제거
print(len(set(n)))