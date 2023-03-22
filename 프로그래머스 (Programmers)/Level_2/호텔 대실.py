import heapq
def solution(book_time):
    answer = 0
    times=list()
    #변환
    for s,e in book_time:
        s_hour,s_min=map(int,s.split(":"))
        e_hour,e_min=map(int,e.split(":"))
        times.append((s_hour*60+s_min,e_hour*60+e_min))
    #시작 시간이 작은대로 정렬
    times.sort() 
    
    extra=0;heap=[]
    for s,e in times:
        while heap and heap[0][0]+10<=s:heapq.heappop(heap);extra+=1
        if extra>0:
            extra-=1
        heapq.heappush(heap,(e,s))
    answer=len(heap)+extra
    return answer