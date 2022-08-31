import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*10 for _ in range(n+1)]
    for i in range(10):dp[1][i]=1
    for i in range(2,n+1):
        for j in range(10):
            if j==0: dp[i][0]=dp[i-1][0]%mod
            else: dp[i][j]=(dp[i][j-1]+dp[i-1][j])%mod
    return sum(dp[n])%mod

if __name__=="__main__":
    mod=10007
    n=int(input())
    print(solve())