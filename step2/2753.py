year=int(input())
#4의 배수 이고 100의 배수가 아닐 때 또는 400의 배수일 때 윤년
if year%4==0 and year%100!=0 or year%400==0:
    print('1')
else:
    print('0')