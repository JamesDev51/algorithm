import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    cnt=1; now_money=limit
    for need in needs:
        if 0<=now_money-need:now_money-=need
        else:now_money=limit-need; cnt+=1    
    return cnt
def solve():
    lt,rt=max(needs),sum(needs)
    res=float('inf') #sum(needs)의 범위가 1e9를 초과해서 inf로 초기화해야됨
    while lt<=rt:
        mid=(lt+rt)//2
        if check(mid)<=m:res=min(res,mid); rt=mid-1 
        else:lt=mid+1
    return res

if __name__=="__main__":
    n,m=map(int,input().split())
    needs=list(int(input()) for _ in range(n))
    print(solve())