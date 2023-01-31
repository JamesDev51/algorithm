from collections import deque
import heapq

def solution(progresses, speeds):
    que=deque()
    for idx, progress in enumerate(progresses):que.append((idx,progress))
    
    answer = []
    heap=[]
    now_completed_idx=0
    
    while que:
        tmp_que=deque()
        count=0
        for idx,progress in que:
            if progress+speeds[idx]<100:tmp_que.append((idx, progress+speeds[idx]))
            else:
                heapq.heappush(heap,idx)
        que=tmp_que
        

        while heap and heap[0]==now_completed_idx:
            count+=1
            now_completed_idx+=1
            heapq.heappop(heap)
        if count>0:answer.append(count)
        que=tmp_que

    return answer