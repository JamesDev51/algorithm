import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def TSP(now, visited):
    if dp[now][visited]!=-1: return dp[now][visited] #이미 현재
    
    ret=float('inf')
    if visited==(1<<n)-1: #base case
        if cost[now][0]!=0: return cost[now][0]
        else: return ret

    dp[now][visited]=float('inf')
    for next in range(n):
        if  visited & 1<<next or cost[now][next]==0:continue
        dp[now][visited]=min(dp[now][visited], TSP(next,visited | 1<<next) + cost[now][next])
    return dp[now][visited]
    
    
if __name__=="__main__":
    n=int(input())
    cost=[list(map(int, input().split())) for _ in range(n)]
    dp=[[-1]*(1<<n) for _ in range(n)]
    print(TSP(0,1))