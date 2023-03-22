import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(100000000)
input=sys.stdin.readline

def TSP(now,visited):
    if dp[now][visited]!=-1:return dp[now][visited]
    if (1<<n) -1 == visited:return cost[now][0] if cost[now][0]!=0 else float('inf')
    dp[now][visited]=float('inf')
    for next in range(n):
        if visited & 1<<next or cost[now][next]==0:continue
        dp[now][visited]=min(dp[now][visited],TSP(next,visited | 1<<next)+cost[now][next])
    return dp[now][visited]
        
if __name__=="__main__":
    n=int(input())
    cost=[list(map(int,input().split())) for _ in range(n)]
    dp=[[-1]*(1<<n) for _ in range(n)] #어떤 node에서 어떤 visited 상태일때의 최소비용
    print(TSP(0,1))