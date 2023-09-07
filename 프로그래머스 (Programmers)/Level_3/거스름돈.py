mod=1_000_000_007

def solution(n, money):
    answer = 0
    dp=[[0]*(n+1) for _ in range(len(money))]
    for i in range(len(money)):
        coin=money[i]
        dp[i][0]=1
        for j in range(1,n+1):
            if j<coin:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=(dp[i-1][j]%mod+dp[i][j-coin]%mod)%mod
    answer=dp[-1][-1]%mod
    return answer