import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq

def dijkstra():
    heap=[]
    heapq.heappush(heap,(0,2))
    while heap:
        dist,node=heapq.heappop(heap)
        if distance[node]<dist:continue
        for next_node,next_dist in graph[node]:
            new_dist=dist+next_dist
            if new_dist<distance[next_node]:
                distance[next_node]=new_dist
                heapq.heappush(heap,(new_dist,next_node))
            if distance[node]<distance[next_node]:
                dp[next_node]+=dp[node]
# def go(node):
#     if dp[node]!=-1: return dp[node]
#     dp[node]=0
#     for next_node, _ in graph[node]:
#         if distance[node]>distance[next_node]:
#             dp[node]+=go(next_node)
#     return dp[node]
if __name__=="__main__":
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    dp=[0]* (n+1);dp[2]=1
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance=[float('inf')]*(n+1); distance[2]=0
    dijkstra()
    print(dp[1])