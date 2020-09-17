a,b,c=map(int,input().split())
'''
손익분기점
c*판매량>a+(b*판매량)
판매량>a/(c-b)
'''
if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)