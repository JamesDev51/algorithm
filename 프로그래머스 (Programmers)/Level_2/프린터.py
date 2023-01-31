import heapq
from collections import deque

def solution(priorities, location):
    answer = 0
    
    heap=[]
    que=deque()
    
    for idx,priority in enumerate(priorities):
        heapq.heappush(heap,-priority)
        que.append((idx,priority))
    
    while True:
        idx,priority=que.popleft()
        largest=-heap[0]
        if priority<largest:que.append((idx,priority))
        else:
            heapq.heappop(heap)
            answer+=1
            if idx==location:break
        
        
    return answer