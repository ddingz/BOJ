h,m=map(int,input().split())
#m이 45분 이상일 때 45분을 빼줌
if m>=45:
    print(h,m-45)
#m이 45분 미만이고 h가 1시 이상일 때 1시간을 빼고 15분을 더해줌
elif m<45 and h>=1:
    print(h-1,m+15)
#m이 45분 미만이고 h가 0시일 때 23시 m분에 15분을 더해줌
else:
    print(23,m+15)