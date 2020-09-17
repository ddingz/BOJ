x=int(input())
y=int(input())
if y>0: #y좌표가 양수
    if x>0: #x좌표가 양수
        print('1')
    else:   #x좌표가 음수
        print('2')
else:   #y좌표가 음수
    if x<0: #x좌표가 음수
        print('3')
    else:   #x좌표가 양수
        print('4')