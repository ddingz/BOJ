dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
w=input()
t=0
for i in w:
    #문자가 dial의 원소 안에 있을 때 그 위치에 3초를 더하여 필요한 시간을 구함
    for j in dial:
        if i in j:
            t+=dial.index(j)+3
print(t)