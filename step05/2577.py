a=int(input())
b=int(input())
c=int(input())
mul=str(a*b*c)
for i in range(10):
    #count(x) list 안에 x의 개수를 반환
    print(mul.count(str(i)))