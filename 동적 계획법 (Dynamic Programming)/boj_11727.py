import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[0]*(n+3)
    dp[1]=1; dp[2]=3
    for i in range(3,n+1):
        dp[i]=(dp[i-1]%mod+(dp[i-2]*2)%mod)%mod
    return dp[n]

if __name__=="__main__":
    n=int(input())
    mod=10007
    print(solve())