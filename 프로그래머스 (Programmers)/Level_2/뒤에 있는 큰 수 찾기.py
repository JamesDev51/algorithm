from collections import deque

def solution(numbers):
    answer = [0]*len(numbers)
    que=deque()
    for idx, value in enumerate(numbers):
        while que and que[-1][0]<value:
            _,poped_idx=que.pop()
            answer[poped_idx]=value
        que.append((value,idx))
    
    while que:
        _,poped_idx=que.popleft()
        answer[poped_idx]=-1
    return answer