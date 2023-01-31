import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>=2 and scoville[0]<K:
        first=heapq.heappop(scoville)
        second=heapq.heappop(scoville)
        heapq.heappush(scoville,first+2*second)
        answer+=1
    if len(scoville)==1 and scoville[0]<K:answer=-1    
    return answer