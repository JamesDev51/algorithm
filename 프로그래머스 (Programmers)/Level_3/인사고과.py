import heapq
def solution(scores):
    answer = -1
    idx_scores=[]
    a_scores=[]
    biggest_a=float('-inf')
    
    for idx,value in enumerate(scores):
        a,b=value
        idx_scores.append((a,b,idx))
        a_scores.append(a)
        biggest_a=max(biggest_a,a)
    idx_scores.sort(key=lambda x:-x[0])
    a_scores.sort()
    a_bigger=dict()
    for i in range(len(a_scores)-1):
        a=a_scores[i]
        a_bigger[a]=a_scores[i+1]
    biggest_value=[float('-inf')]*100001
    for a,b,_ in idx_scores:
        if a==biggest_a:
            biggest_value[a]=max(biggest_value[a],b)
        else:
            biggest_value[a]=max(biggest_value[a],b,biggest_value[a_bigger[a]])
    heap=[]
    for a,b,idx in idx_scores:
        if a==biggest_a:
            heapq.heappush(heap,(-(a+b),idx))
        else:
            if b>=biggest_value[a_bigger[a]]:
                heapq.heappush(heap,(-(a+b),idx))
    
    answer=-1
    prev_score=float('-inf')
    rank=0
    acc=0
    while heap:
        score,idx=heapq.heappop(heap)
        if score==prev_score:acc+=1
        else:
            rank+=(acc+1)
            acc=0
        prev_score=score
        if idx==0:answer=rank;break

    return answer