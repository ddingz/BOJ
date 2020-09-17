#sys.stdin.readline() input()에 비해 시간절약
import sys
t=int(sys.stdin.readline())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)