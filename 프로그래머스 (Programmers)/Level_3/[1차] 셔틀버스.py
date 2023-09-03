from collections import deque
import heapq

def convert_number(timetable):
    heap=[]
    for time in timetable:
        hour,minute=map(int,time.split(":"))
        heapq.heappush(heap,hour*60+minute)
    return heap

def convert_time(time_number):
    hour=str(time_number//60) if 10<=time_number//60 else "0"+str(time_number//60)
    minute=str(time_number%60) if 10<=time_number%60 else "0"+str(time_number%60)
    return f"{hour}:{minute}"

def get_bus_time(n,t,m,heap):
    answer=0
    last_time=0
    now_time=60*9
    for _ in range(n):
        cnt=0
        while heap and heap[0]<=now_time and cnt<m:
            user_time=heapq.heappop(heap)
            last_time=max(last_time,user_time)
            cnt+=1
        if cnt<m: #아직 자리가 있어서 탈 수 있는 경우
            answer=max(answer,now_time)
        else: #자리가 없는 경우
            answer=max(answer,last_time-1)
        now_time+=t
        
    return convert_time(answer)
        


def solution(n, t, m, timetable):
    heap=convert_number(timetable)
    answer = get_bus_time(n,t,m,heap)
    
    return answer