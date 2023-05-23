import heapq
def solution(operations):
    answer = []
    num_set=set()
    max_heap=[]
    min_heap=[]
    for operation in operations:
        com,num = operation.split(" ")
        num=int(num)
        if com=="I":
            num_set.add(num)
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
        else:
            if num==1:
                while max_heap:
                    poped=-heapq.heappop(max_heap)
                    if poped in num_set:num_set.remove(poped);break
            else:
                while min_heap:
                    poped=heapq.heappop(min_heap)
                    if poped in num_set:num_set.remove(poped);break
    largest,smallest=0,0
    while max_heap:
        poped=-heapq.heappop(max_heap)
        if poped in num_set:largest=poped;break
    while min_heap:
        poped=heapq.heappop(min_heap)
        if poped in num_set:smallest=poped;break
    answer=[largest,smallest]
        
    return answer