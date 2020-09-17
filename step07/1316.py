cnt=0
for _ in range(int(input())):
    w=input()
    #sorted(w,key=w.find) 문자열에서 찾아지는 문자 순으로 정렬
    if list(w)==sorted(w,key=w.find):
        cnt+=1
print(cnt)