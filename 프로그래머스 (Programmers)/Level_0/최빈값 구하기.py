import heapq
def solution(array):
    h=[0]*1000
    for num in array:
        h[num]+=1
    heap=[]
    for idx in range(1000):
        if h[idx]!=0: 
            heapq.heappush(heap,(-h[idx],idx))
    if len(heap)==1:
        cnt,num=heapq.heappop(heap)
        return num
    else:
        cnt1,num1=heapq.heappop(heap)
        cnt2,num2=heapq.heappop(heap)
        return num1 if cnt1!=cnt2 else -1