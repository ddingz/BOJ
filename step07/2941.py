cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
w=input()
for i in cro:
    #replace(바뀌게 될 문자열, 바꿀 문자열) 문자열 안의 특정한 값을 다른 값으로 치환
    w=w.replace(i,'@')
print(len(w))