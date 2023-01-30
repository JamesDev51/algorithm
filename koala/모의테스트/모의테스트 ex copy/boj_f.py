import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq

def dijkstra(start):
    distance=[float('inf')]*(n+1); distance[start]=0
    heap=[]; heapq.heappush(heap,(0,start))
    while heap:
        now_cost,now_node=heapq.heappop(heap)
        if distance[now_node]<now_cost: continue
        for next_node,next_cost in graph[now_node]:
            new_total_cost=now_cost+next_cost
            if new_total_cost<distance[next_node]:
                distance[next_node]=new_total_cost
                heapq.heappush(heap,(new_total_cost,next_node))
    if start==x: return distance
    return distance[x]
                
    

if __name__=="__main__":
    n,m,x=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,cost=map(int,input().split())
        graph[a].append((b,cost))
    answer=float('-inf')
    ret_cost=dijkstra(x)
    for node in range(1,n+1):
        if node==x:continue
        answer=max(answer,dijkstra(node)+ret_cost[node])
    print(answer)