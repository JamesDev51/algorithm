from collections import deque

def solution(bridge_length, weight, truck_weights):
    que=deque()
    now=0
    sub_sum=0
    for truck in truck_weights:
        while len(que)+1>bridge_length or sub_sum+truck>weight:
            now+=1
            if now-que[0][1]>=bridge_length:
                out_truck,in_time=que.popleft()
                sub_sum-=out_truck
        que.append((truck,now))
        sub_sum+=truck
    while que:
        now+=1
        if now-que[0][1]>=bridge_length:
            que.popleft()
    now+=1
    return now