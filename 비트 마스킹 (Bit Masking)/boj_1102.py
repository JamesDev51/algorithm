import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(status,cnt):
    if dp[status]!=-1: return dp[status]
    
    if p<=cnt: return 0
    
    dp[status]=float('inf')
    for i in range(n):
        for j in range(n):
            if status& 1<<i and status^ 1<<j:
                dp[status]=min(dp[status],solve(status | 1<<j,cnt+1)+cost[i][j])
    return dp[status]


if __name__=="__main__":
    n=int(input())
    cost=[list(map(int,input().split())) for _ in range(n)]
    str_status=input().strip()
    p=int(input())
    status=0; cnt=0
    for i in range(n): 
        if str_status[i]=='Y' :status |= 1<<i ;cnt+=1
    dp=[-1]*(1<<n)
    res=solve(status,cnt)
    print(res if res!=float('inf') else -1)