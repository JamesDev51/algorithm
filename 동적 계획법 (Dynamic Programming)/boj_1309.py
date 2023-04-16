import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MOD=9901
if __name__=="__main__":
    n=int(input())
    dp=[[0]*2 for _ in range(n+1)]
    dp[1]=[3,2]
    for i in range(2,n+1):
        dp[i][1]=(dp[i-1][0]*2-dp[i-1][1])%MOD
        dp[i][0]=(dp[i-1][0]+dp[i][1])%MOD
    print(dp[n][0])