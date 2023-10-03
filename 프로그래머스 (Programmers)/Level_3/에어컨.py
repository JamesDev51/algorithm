def solution(temperature, t1, t2, a, b, onboard):
    answer = float('inf')
    smallest=min(temperature,t1,t2)
    temperature-=smallest
    t1-=smallest
    t2-=smallest
    largest=max(temperature,t1,t2)
    
    if temperature==0:direction=True #up
    else:direction=False #down
    
    
    dp=[[float('inf')]*(len(onboard)) for _ in range(largest+1)]
    dp[temperature][0]=0
    for j in range(1,len(onboard)):
        for i in range(largest+1):
            if onboard[j]==1 and not t1<=i<=t2:continue
            if i==0:
                dp[i][j]=min(dp[i][j-1] if i==temperature else float('inf'),dp[i][j-1]+b,dp[i+1][j-1]+a if not direction else dp[i+1][j-1])
            elif i==largest:
                dp[i][j]=min(dp[i][j-1] if i==temperature else float('inf'),dp[i][j-1]+b,dp[i-1][j-1]+a if direction else dp[i-1][j-1])
            else:
                dp[i][j]=min(dp[i][j-1] if i==temperature else float('inf'),dp[i][j-1]+b,dp[i+1][j-1]+a if not direction else dp[i+1][j-1],dp[i-1][j-1]+a if direction else dp[i-1][j-1])
    

    
    last_idx=0
    for j in range(len(onboard)):
        if onboard[j]==1:last_idx=j
    for i in range(t1,t2+1):
        answer=min(answer,dp[i][last_idx])
    
    return answer