import heapq
def solution(A, B):
    answer = 0
    A.sort()
    heapq.heapify(B)
    for a in A:
        while B:
            poped=heapq.heappop(B)
            if a<poped:
                answer+=1;break

    return answer