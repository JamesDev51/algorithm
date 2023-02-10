MOD=1000000007

def solution(n):
    answer = 0
    dp=[0]*60001
    dp[1]=1
    dp[2]=2
    if n>=3:
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+dp[i-2])%MOD

    return dp[n]%MOD