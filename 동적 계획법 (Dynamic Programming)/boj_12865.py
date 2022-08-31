import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*(k+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w,v=items[i-1]
        for j in range(1,k+1):
            if w<=j:dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-w]+v)
            else:dp[i][j]=dp[i-1][j]
    return dp[n][k]
            
            

if __name__=="__main__":
    n,k=map(int,input().split())
    items=[list(map(int,input().split())) for _ in range(n)]
    print(solve())