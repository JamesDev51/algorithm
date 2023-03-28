import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations as com

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    a=list();b=list()
    for y in range(n):
        for x in range(n):
            if mat[y][x]==1:a.append((y,x))
            if mat[y][x]==2:b.append((y,x))
    res=float('inf')
    for comb in com(b,m):
        dist=0
        for hy,hx in a:
            smallest=float('inf')
            for cy,cx in comb:
                smallest=min(smallest,abs(hy-cy,)+abs(hx-cx))
            dist+=smallest
        res=min(res,dist)
    print(res)
            