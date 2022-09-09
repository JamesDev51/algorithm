import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    cnt_sum=0
    for a,b,c in rules:
        if limit<a<=b:continue
        elif a==limit: cnt_sum+=1
        elif a<limit<b:cnt_sum+=((limit-a)//c+1)
        elif b<=limit:cnt_sum+=((b-a)//c+1)
    return cnt_sum

def solve():
    lt,rt=1,n
    res=float('inf')
    while lt<=rt:
        mid=(lt+rt)//2
        if d<=check(mid):
            res=min(res,mid);rt=mid-1
        else:lt=mid+1
    return res

if __name__=="__main__":
    n,k,d=map(int, input().split())
    rules=[list(map(int,input().split()) ) for _ in range(k)]
    print(solve())