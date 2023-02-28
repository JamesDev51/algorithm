import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq

def dijkstra(start_node):
    distance[start_node][start_node]=0
    heap=[]
    heapq.heappush(heap,(0,start_node))
    while heap:
        cost,node=heapq.heappop(heap)
        if distance[start_node][node]<cost:continue
        for next_node,next_cost in graph[node]:
            new_cost=cost+next_cost
            if new_cost<distance[start_node][next_node]:
                distance[start_node][next_node]=new_cost
                heapq.heappush(heap,(new_cost,next_node))

if __name__=="__main__":
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    distance=[[float('inf')]*(n+1) for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for start_node in range(1,n+1):dijkstra(start_node)
    for _ in range(m):
        a,b=map(int,input().split())
        print(distance[a][b])