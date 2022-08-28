import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*10 for _ in range(n+1)]
    for i in range(1,10):dp[1][i]=1
    for i in range(2,n+1):
        for j in range(10):
            if j==0: dp[i][0]=(dp[i-1][1])%mod
            elif j==9: dp[i][9]=(dp[i-1][8])%mod
            else: dp[i][j]=((dp[i-1][j-1])%mod+(dp[i-1][j+1])%mod)%mod
    return sum(dp[n])%mod

if __name__=="__main__":
    mod=1000000000
    n=int(input())
    print(solve())