a,b=map(int,input().split())
if a<b:     #a가 b보다 작을 때
    print('<')
elif a>b:   #a가 b보다 클 때
    print('>')
else:       #a와 b가 같을 때
    print('==')