import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq

def dijkstra():
    dist=[[float('inf')]*(k+1) for _ in range(n+1)]
    dist[1]=[0]*(k+1)
    heap=[]
    heapq.heappush(heap,(0,1,k))
    
    while heap:
        cost,node,cnt=heapq.heappop(heap)
        for next_node,next_cost in graph[node]:
            if max(cost,next_cost)<dist[next_node][cnt]:
                dist[next_node][cnt]=max(cost,next_cost)
                heapq.heappush(heap,(dist[next_node][cnt],next_node,cnt))
            if 0<cnt and cost<dist[next_node][cnt-1]:
                dist[next_node][cnt-1]=cost
                heapq.heappush(heap,(dist[next_node][cnt-1],next_node,cnt-1))
    return min(dist[n]) if min(dist[n])!=float('inf') else -1
        
if __name__=="__main__":
    n,p,k=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(p):
        n1,n2,cost=map(int,input().split())
        graph[n1].append((n2,cost))
        graph[n2].append((n1,cost))
    print(dijkstra())