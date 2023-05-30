def solution(n, s):
    answer = []
    if s<n:answer=[-1]
    else:
        val=s//n
        left=s%n
        answer=[val]*n
        for i in range(1,left+1):answer[-i]+=1
    return answer