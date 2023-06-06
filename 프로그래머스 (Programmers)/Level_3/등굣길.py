MOD=1000000007
def solution(m, n, puddles):
    answer = 0
    dp=[[0]*(m+1) for _ in range(n+1)]
    for x,y in puddles: dp[y][x]=float('-inf')

    dp[1][1]=1
    for y in range(2,n+1):dp[y][1]+=dp[y-1][1]
    for x in range(2,m+1):dp[1][x]+=dp[1][x-1]
    for y in range(2,n+1):
        for x in range(2,m+1):
            if dp[y][x]==float('-inf'):continue
            dp[y][x]=(dp[y-1][x] if dp[y-1][x]!=float('-inf') else 0)%MOD + (dp[y][x-1] if dp[y][x-1]!=float('-inf') else 0)%MOD
        
    answer=dp[-1][-1]%MOD
    return answer