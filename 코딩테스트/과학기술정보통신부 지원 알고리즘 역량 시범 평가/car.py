import sys
input=sys.stdin.readline
from bisect import bisect_left,bisect_right

if __name__=="__main__":
    k,m=map(int,input().split())
    stations=list(map(int,input().split()))
    stations.sort()
    for _ in range(m):
        p,c=map(int,input().split())
        lt,rt=p-c,p+c
        print(bisect_right(stations,rt)-bisect_left(stations,lt))
    