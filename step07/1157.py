w=input().upper()
cnt=[]
for i in set(w):
    cnt.append(w.count(i))
#enumerate 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
idx=[i for i,x in enumerate(cnt) if x==max(cnt)]
if len(idx)>1:
    print('?')
else:
    print(list(set(w))[cnt.index(max(cnt))])