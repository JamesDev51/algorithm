import heapq
def solution(n, paths, gates, summits):
    def dijkstra(start_summit):
        distance=[float('inf')]*(n+1)
        distance[start_summit]=0
        heap=[]
        heapq.heappush(heap,(0,start_summit))
        
        while heap:
            now_dist,now_node=heapq.heappop(heap)
            if info[now_node]==0:continue #gate에서는 더 이상 진행 x 
            for next_node,next_dist in graph[now_node]:
                if info[next_node]==2:continue
                if max(now_dist,next_dist)<distance[next_node] and max(now_dist,next_dist)<answer[1]:
                    distance[next_node]=max(now_dist,next_dist)
                    heapq.heappush(heap,(distance[next_node],next_node))
        for gate in gates:
            if distance[gate]<answer[1]:
                answer[0]=start_summit
                answer[1]=distance[gate]
        
           
    answer=[-1,1e9] 
        
    graph=[[] for _ in range(n+1)]
    info=[1]*(n+1)
    for gate in gates:
        info[gate]=0
    for summit in summits:
        info[summit]=2
    
    shortest_dist=float('inf')
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    
    summits.sort()
    for summit in summits:
        dijkstra(summit)

    
    return answer