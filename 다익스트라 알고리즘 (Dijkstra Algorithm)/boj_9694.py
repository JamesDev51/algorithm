import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

import heapq
def dijkstra():
    dist=[float('inf')]*m
    dist[0]=0
    before=[-1]*m
    heap=[]
    heapq.heappush(heap,(0,0))
    while heap:
        d,node=heapq.heappop(heap)
        if dist[node]<d:continue
        for next_node,next_d in graph[node]:
            if d+next_d<dist[next_node]:
                dist[next_node]=d+next_d
                before[next_node]=node
                heapq.heappush(heap,(dist[next_node],next_node))
    if dist[m-1]==float('inf'):print(-1)
    else:
        ret=""
        stack=[]
        node=m-1
        stack.append(m-1)
        while True:
            node=before[node]
            stack.append(node)
            if node==0:break
        while stack:
            print(stack.pop(),end=" ")

            
                

if __name__=="__main__":
    for t in range(1,int(input())+1):
        n,m=map(int,input().split())
        graph=[[] for _ in range(m)]
        for _ in range(n):
            x,y,z=map(int,input().split())
            graph[x].append((y,z))
            graph[y].append((x,z))
        print(f"Case #{t}: ",end="")
        dijkstra()
        print()
        
        