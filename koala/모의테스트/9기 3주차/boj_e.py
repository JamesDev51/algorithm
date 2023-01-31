import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

def convert_time(time):
    return 60*int(time[:2])+int(time[2:])

def organize():
    for seat in range(1,n+1):
        e_hour,e_min=used[seat]
        if 60*e_hour+e_min<=60*now_hour+now_min:used[seat]=0

def get_new_seat():
    heap=[]
    min_distance=[float('inf')]*(n+1)
    for seat in range(1,n+1):
        if used[seat]: #사용중인 자리
            for next_seat in range(1,n+1):
                if seat==next_seat or used[next_seat]>0:continue
                min_distance[next_seat]=min(min_distance[next_seat],abs(seat-next_seat))
    for seat in range(1,n+1):
        if min_distance[seat]!=float('inf'):heapq.heappush(heap,(-min_distance[seat],seat))
    return heap[0][1] if heap else 1

def solve():
    total_use=0
    heap=[]
    for start,end in times:
        s=convert_time(start)
        e=convert_time(end)
        
        while heap and heap[0][0]<=s:#일어나야 할 이벤트를 먼저 처리함
            time,seat =heapq.heappop(heap)
            used[seat]=0
        
        new_seat=get_new_seat() #새로운 자리 할당
    
        if new_seat==p:
            gap=s-end_time_table[p] #빈 시간 
            total_use+=gap #민규가 이용한 시간
        
        used[new_seat]=1
        end_time_table[new_seat]=e #끝나는 시간 입력
        heapq.heappush(heap,(e,new_seat))
    return total_use+(21*60-end_time_table[p])
        

if __name__=="__main__":
    n,t,p=map(int, input().split())
    times=[list(input().strip().split()) for _ in range(t)]
    times.sort()
    used=[0]*(n+1)
    end_time_table=[0]*(n+1); end_time_table[p]=540
    print(solve())