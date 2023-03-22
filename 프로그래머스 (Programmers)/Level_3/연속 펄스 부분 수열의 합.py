from copy import deepcopy
def go(arr):
    dp=[0]*len(arr)
    dp[0]=arr[0]
    for i in range(1,len(arr)):
        dp[i]=max(0,dp[i-1])+arr[i]
    return max(dp)
        

def solution(sequence):
    answer = 0
    case1=deepcopy(sequence)
    for i in range(len(sequence)):
        if i%2==0:case1[i]*=(-1)
    answer=max(answer,go(case1))
    case2=deepcopy(sequence)
    for i in range(len(sequence)):
        if i%2==1:case2[i]*=(-1)
    answer=max(answer,go(case2))
    return answer
