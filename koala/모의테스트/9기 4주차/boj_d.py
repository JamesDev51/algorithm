import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

    

def dijkstra():
    distance=[[float('inf')]*11 for _ in range(n+1)]; distance[1][1]=0
    heap=[]
    heapq.heappush(heap,(0, 1, 1)) #시간, 속도, 노드
    while heap:
        now_time, now_speed, now_node=heapq.heappop(heap)
        
        for new_node,length,limit in graph[now_node]:
            for new_speed in range(now_speed-1,now_speed+2):
                if new_speed<1 or limit<new_speed:continue
                new_time=now_time+length/new_sp
                if (new_time<distance[new_node][new_speed]):
                    distance[new_node][new_speed]=new_time
                    heapq.heappush(heap,(new_time,new_speed, new_node))
    return min(distance[n])
    

if __name__=="__main__":
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,l,k=map(int, input().split())
        graph[a].append((b,l*2520,k))
        graph[b].append((a,l*2520,k))
    print("{:.9f}".format(dijkstra()/2520))