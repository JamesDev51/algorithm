def solution(triangle):
    answer = 0
    size=len(triangle[-1])
    dp=[[0]*(size) for _ in range(size)]
    dp[0][0]=triangle[0][0]
    for i in range(1,size):
        for j in range(i+1):
            dp[i][j]=triangle[i][j]+max(dp[i-1][j-1] if 0<=j-1<i else float('-inf'), dp[i-1][j] if 0<=j<i else float('-inf'))
    answer=max(dp[-1])
            
    return answer