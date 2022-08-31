import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    sub_sum=0
    for need in needs:
        sub_sum+= (need if need<limit else limit)
    return True if sub_sum<=budget else False

def solve():
    lt,rt=0,max(needs)
    res=-1e9
    while lt<=rt:
        mid=(lt+rt)//2
        if check(mid):
            res=max(res,mid)
            lt=mid+1
        else: rt=mid-1
    return res

if __name__=="__main__":
    n=int(input())
    needs=list(map(int,input().split()))
    budget=int(input())
    print(max(needs) if sum(needs)<=budget else solve())