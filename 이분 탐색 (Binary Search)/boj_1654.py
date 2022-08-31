import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    cnt=0
    for line in lines:
        cnt+=line//limit
    return cnt
def solve():
    lt,rt=1,max(lines)
    res=float('-inf')
    while lt<=rt:
        mid=(lt+rt)//2
        if n<=check(mid): res=max(res,mid); lt=mid+1
        else: rt=mid-1
    return res

if __name__=="__main__":
    k,n=map(int,input().split())
    lines=list(int(input()) for _ in range(k))
    print(solve())