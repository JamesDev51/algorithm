from collections import deque
def solution(s):
    length=len(s)
    answer = length
    for cut in range(1,length//2+1):
        que=deque()
        idx=0
        while idx<length:
            part=s[idx:idx+cut]
            if que and que[-1][0]==part:que[-1][1]+=1
            else:que.append([part,1])
            idx+=cut
        tmp=""
        while que:
            alphas,num=que.popleft()
            if num==1:tmp+=alphas
            else:tmp=tmp+str(num)+alphas
        answer=min(answer,len(tmp))
        
    return answer