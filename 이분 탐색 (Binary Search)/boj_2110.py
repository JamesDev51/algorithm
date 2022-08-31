import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    now=

def solve():
    lt,rt=1,max(houses)
    res=float('-inf')
    while lt<=rt:
        mid=(lt+rt)//2
        if c<=check(mid):res=max(res,mid); lt=mid+1
        else: rt=mid-1
    return res
if __name__=="__main__":
    n,c=map(int,input().split())
    houses=list(int(input()) for _ in range(n))
    houses.sort()
    print(solve())