import heapq

def solution(k, score):
    answer = []
    heap=[]
    for s in score:
        if len(heap)<k:heapq.heappush(heap,s)
        else:
            if heap[0]<s:
                heapq.heappop(heap)
                heapq.heappush(heap,s)
        answer.append(heap[0])
    return answer