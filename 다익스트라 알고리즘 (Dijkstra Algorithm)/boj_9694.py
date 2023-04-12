import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

import heapq
def dijkstra():
    dist=[float('inf')]*m
    dist[0]=0
    heap=[]
    heapq.heappush(heap,(0,0))
    while heap:
        d,node=heapq.heappop(heap)
        if dist[node]<d:continue
        for next_node,next_d in graph[node]:
            if d+next_d<dist[next_node]:
                dist[next_node]=d+next_d
                heapq.heappush(heap,(dist[next_node],next_node))
    if dist[m-1]==float('inf'):ret="-1"
    else:
        ret=""
        stack=[]
        stack.append((0,0,"0"))
        while stack:
            now_node,d,line=stack.pop()
            if d>dist[m-1]:continue
            if now_node==m-1 and d==dist[m-1]:
                ret=line
                break
            for next_node,next_d in graph[now_node]:
                if str(next_node) in line:continue
                stack.append((next_node,d+next_d,line+" "+str(next_node)))

    return ret

if __name__=="__main__":
    for t in range(1,int(input())+1):
        n,m=map(int,input().split())
        graph=[[] for _ in range(m)]
        for _ in range(n):
            x,y,z=map(int,input().split())
            graph[x].append((y,z))
            graph[y].append((x,z))
        print(f"Case #{t}: {dijkstra()}")
        
        