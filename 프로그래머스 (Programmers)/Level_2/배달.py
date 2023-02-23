import heapq

def init(n,road):
    graph=[[] for _ in range(n+1)]
    for n1,n2,cost in road:
        graph[n1].append((n2,cost))
        graph[n2].append((n1,cost))
    return graph
    
def dijkstra(n,graph,k):
    heap=list(); heapq.heappush(heap,(0,1))
    distance=[float('inf')]*(n+1); distance[1]=0
    while heap:
        cost,node=heapq.heappop(heap)
        if distance[node]<cost: continue
        for next_node,next_cost in graph[node]:
            new_cost=cost+next_cost
            if new_cost<distance[next_node]:
                distance[next_node]=new_cost
                heapq.heappush(heap,(new_cost,next_node))
    ret=1
    for node in range(2,n+1):
        if distance[node]<=k:ret+=1
    return ret
    
def solution(N, road, K):
    graph=init(N,road)
    answer=dijkstra(N,graph,K)
    
    return answer