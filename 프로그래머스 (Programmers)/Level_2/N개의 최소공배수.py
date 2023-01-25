from math import gcd
from collections import deque

def solution(arr):
    que=deque(arr)
    while len(que)>1:
        n1,n2=que.popleft(),que.popleft()
        que.append(n1*n2//gcd(n1,n2))
    answer=que[0]
    return answer