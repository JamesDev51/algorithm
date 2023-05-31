import heapq

def solution(n, works):
    answer = 0
    heap=[]
    for work in works:
        heapq.heappush(heap,-work)
    for _ in range(n):
        if not heap:break
        largest=-heapq.heappop(heap)
        if largest-1>0:heapq.heappush(heap,-(largest-1))
        else:continue
    if heap:
        for work in heap:
            answer+=pow(work,2)
            
    return answer