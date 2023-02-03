def solution(land):
    answer = 0
    dp=[[0]*4 for _ in range(len(land))]
    dp[0]=land[0]
    for i in range(1,len(land)):
        for j in range(4):
            for k in range(4):
                if j!=k:dp[i][j]=max(dp[i][j],dp[i-1][k]+land[i][j])
    answer=max(dp[-1])
                    

    return answer