#map(int,input().split()) 공백을 기준으로 나눠서 int형으로 저장
a,b,c=map(int,input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)