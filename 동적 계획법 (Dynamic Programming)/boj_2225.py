import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


MOD=10**9
if __name__=="__main__":
    n,k=map(int,input().split())
    dp=[[0]*(n+1) for _ in range(k+1)]
    for i in range(n+1):dp[1][i]=1
    for i in range(k+1):dp[i][0]=1
    for i in range(2,k+1):
        for j in range(1,n+1):
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%MOD
    print(dp[-1][-1])
            