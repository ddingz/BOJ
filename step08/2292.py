'''
1+6+12+18+24+30+36...
위와 같이 벌집 방이 증가할 때마다 최소 개수가 1씩 증가
'''
n=int(input())
cnt=1
room=1
six=0
while n>room:
    cnt+=1
    six+=6
    room+=six
print(cnt)