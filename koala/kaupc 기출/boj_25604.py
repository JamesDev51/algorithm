import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def solution():
    time=0;truck_loc=0;truck_weight=0
    while que0 or que1: #모든 부품이 없을때까지 반복
        if truck_loc==0 and not que0:truck_loc=1;time+=t
        elif truck_loc==1 and not que1:truck_loc=0;time+=t
        while (que0 and que0[0][1]>time) and (que1 and que1[0][1]>time):time+=1 #가능한 경우 만들기
        if (que0 and que0[0][1]<=time) and (que1 and que1[0][1]<=time): #둘 다 가능한 경우 -> 트럭 위치에 따라서 옮기기
            if truck_loc==0:
                while que0 and que0[0][1]<=time and truck_weight<truck_limit:
                    m,r,i=que0.popleft()
                    if truck_weight+m<=truck_limit:
                        start_time[i]=min(start_time[i],time)
                        truck_weight+=m #전부 다 가능
                        end_time[i]=time+t
                    else:
                        gap=truck_limit-truck_weight #옮길 수 있는 양
                        truck_weight+=gap
                        start_time[i]=min(start_time[i],time)
                        que0.appendleft((m-gap,r,i))
                truck_loc=1
                time+=t
                truck_weight=0
            else:
                while que1 and que1[0][1]<=time and truck_weight<truck_limit:
                    m,r,i=que1.popleft()
                    if truck_weight+m<=truck_limit:
                        start_time[i]=min(start_time[i],time)
                        truck_weight+=m #전부 다 가능
                        end_time[i]=time+t
                    else:
                        gap=truck_limit-truck_weight #옮길 수 있는 양
                        truck_weight+=gap
                        start_time[i]=min(start_time[i],time)
                        que1.appendleft((m-gap,r,i))
                truck_loc=0
                time+=t
                truck_weight=0
        elif que0 and que0[0][1]<=time:
            if truck_loc==1:time+=t;truck_loc=0
            while que0 and que0[0][1]<=time and truck_weight<truck_limit:
                m,r,i=que0.popleft()
                if truck_weight+m<=truck_limit:
                    start_time[i]=min(start_time[i],time)
                    truck_weight+=m #전부 다 가능
                    end_time[i]=time+t
                else:
                    gap=truck_limit-truck_weight #옮길 수 있는 양
                    truck_weight+=gap
                    start_time[i]=min(start_time[i],time)
                    que0.appendleft((m-gap,r,i))
            truck_loc=1
            time+=t
            truck_weight=0
        elif que1 and que1[0][1]<=time:
            if truck_loc==0:time+=t;truck_loc=1
            while que1 and que1[0][1]<=time and truck_weight<truck_limit:
                m,r,i=que1.popleft()
                if truck_weight+m<=truck_limit:
                    start_time[i]=min(start_time[i],time)
                    truck_weight+=m #전부 다 가능
                    end_time[i]=time+t
                else:
                    gap=truck_limit-truck_weight #옮길 수 있는 양
                    truck_weight+=gap
                    start_time[i]=min(start_time[i],time)
                    que1.appendleft((m-gap,r,i))
            truck_loc=0
            time+=t
            truck_weight=0
        elif que1 and not que0:
            time=que1[0][1]
            if truck_loc==0:time+=t;truck_loc=1
            while que1 and que1[0][1]<=time and truck_weight<truck_limit:
                m,r,i=que1.popleft()
                if truck_weight+m<=truck_limit:
                    start_time[i]=min(start_time[i],time)
                    truck_weight+=m #전부 다 가능
                    end_time[i]=time+t
                else:
                    gap=truck_limit-truck_weight #옮길 수 있는 양
                    truck_weight+=gap
                    start_time[i]=min(start_time[i],time)
                    que1.appendleft((m-gap,r,i))
            truck_loc=0
            time+=t
            truck_weight=0
        elif que0 and not que1:
            time=que0[0][1]
            if truck_loc==1:time+=t;truck_loc=0
            while que0 and que0[0][1]<=time and truck_weight<truck_limit:
                m,r,i=que0.popleft()
                if truck_weight+m<=truck_limit:
                    start_time[i]=min(start_time[i],time)
                    truck_weight+=m #전부 다 가능
                    end_time[i]=time+t
                else:
                    gap=truck_limit-truck_weight #옮길 수 있는 양
                    truck_weight+=gap
                    start_time[i]=min(start_time[i],time)
                    que0.appendleft((m-gap,r,i))
            truck_loc=1
            time+=t
            truck_weight=0
        
if __name__=="__main__":
    n,truck_limit,t=map(int,input().split())
    que0,que1=deque(),deque()
    start_time=[float('inf')]*n
    end_time=[float('inf')]*n

    for i in range(n):
        d,m,r=map(int,input().split())
        if d==0:que0.append((m,r,i))
        else:que1.append((m,r,i))
    solution()
    for i in range(n):
        print(start_time[i],end_time[i])
    