a=int(input())
b=int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))   #// 나눗셈의 몫을 구함
print(a*b)