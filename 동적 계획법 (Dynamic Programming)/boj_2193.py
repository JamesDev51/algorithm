import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*2 for _ in range(n+1)]; dp[1][1]=1
    for i in range(2,n+1):
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]
    return dp[n][0]+dp[n][1]

if __name__=="__main__":  
    n=int(input())
    print(solve())