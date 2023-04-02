import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import math

def calculate(limit):
    cnt=0
    for i in range(len(gaps)):
        j=1
        while math.ceil(gaps[i])/j>limit:j+=1
        cnt+=(j-1)
    return cnt

if __name__=="__main__":
    n,m,l=map(int,input().split())
    locs=list(map(int,input().split()))
    locs.insert(0,0)
    locs.append(l)
    locs.sort()
    gaps=[locs[i]-locs[i-1] for i in range(1,n+2)]
    lt,rt=1,max(gaps)
    res=1e9
    while lt<=rt:
        mid=(lt+rt)//2
        need_cnt=calculate(mid)
        if need_cnt<=m:
            rt=mid-1
            res=min(res,mid)
        else:lt=mid+1
    print(res)
    