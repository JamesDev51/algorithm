import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


MOD=10**9
if __name__=="__main__":
    n=int(input())
    dp=[0]*(n+1)
    for i in range(2,n+1):
        if i%2==0:
            dp[i]=(i*dp[i-1]+1)%MOD
        else:
            dp[i]=(i*dp[i-1]-1)%MOD
    print(dp[n])
            