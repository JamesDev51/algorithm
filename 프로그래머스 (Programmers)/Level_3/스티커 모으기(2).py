def solution(sticker):
    answer = 0
    n=len(sticker)
    if n<=3:return max(sticker) #3개 이하면 하나밖에 못 뗌
    dp=[0]*n
    dp[0]=sticker[0]
    dp[1]=max(sticker[0:2])
    for i in range(2,n-1):
        dp[i]=max(dp[i-2]+sticker[i],dp[i-1])
    answer=max(dp)
    
    dp=[0]*n
    dp[1]=sticker[1]
    for i in range(2,n):
        dp[i]=max(dp[i-2]+sticker[i],dp[i-1])
    answer=max(answer,max(dp))        
    
    return answer