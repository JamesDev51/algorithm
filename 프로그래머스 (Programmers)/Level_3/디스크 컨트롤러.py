import heapq

def solution(jobs):
    answer = 0
    heap=[]
    jobs.sort()
    time=jobs[0][0]
    idx=0
    while idx<len(jobs) or heap:
        if not heap and time<jobs[idx][0]:time=jobs[idx][0]
        while idx<len(jobs) and jobs[idx][0]<=time:
            heapq.heappush(heap,(jobs[idx][1],jobs[idx][0]))
            idx+=1
        dur,req=heapq.heappop(heap)
        time=max(time,req)+dur
        answer+=(time-req)
    answer//=len(jobs)
        
    return answer