import sys
sys.stdin = open("input.text",  "rt")
import sys
import math
input=sys.stdin.readline

def solve():
    dp=[[0]*1001 for _ in range(1001)]
    dp[1][0]=1; dp[1][1]=1
    for i in range(2,n+1):
        for j in range(i+1):
            if j==0 or j==i:dp[i][j]=1
            else:dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%mod
    return dp[n][k]%mod
            
if __name__=="__main__":
    n,k=map(int,input().split())
    mod=10007
    print(solve())