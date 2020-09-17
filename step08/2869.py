a,b,v=map(int,input().split())
'''
a*day-b(day-1)>=v
day>=(v-b)/(a-b)
(v-b-1)//(a-b)+1 정수로 구하기 위한 변형
'''
print((v-b-1)//(a-b)+1)