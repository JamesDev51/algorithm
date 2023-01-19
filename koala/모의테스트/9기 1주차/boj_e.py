import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

def dijkstra(start):
    global x
    costs=[float('inf')]*(n+1)
    costs[start]=0
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        now_cost,now_node=heapq.heappop(heap)
        if costs[now_node]<now_cost: continue
        for next_cost,next_node in graph[now_node]:
            if now_cost+next_cost<costs[next_node]:
                costs[next_node]=now_cost+next_cost
                heapq.heappush(heap,(costs[next_node],next_node))
    if start==x:
        for node in range(1,n+1): total_costs[node]+=costs[node]
    else:
        total_costs[start]+=costs[x]
    

if __name__=="__main__":
    n,m,x=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t=map(int,input().split())
        graph[s].append((t,e))
    total_costs=[0]*(n+1)
    for i in range(1,n+1): 
        dijkstra(i)
    print(max(total_costs))
        
    
    