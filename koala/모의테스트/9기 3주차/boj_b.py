import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq
from copy import deepcopy

if __name__=="__main__":
    n,m=map(int,input().split())
    c=[0]+list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    for _ in range(int(input())):
        a,b,t,=map(int,input().split())
        graph[a].append((b,t)) #하향 가능한 곳
        c[b]+=t
        
    heap=[]
    for idx in range(1,n+1): heapq.heappush(heap,(c[idx],idx))
    ch=[0]*(n+1)
    
    answer=-1
    while m:
        poped,node=heapq.heappop(heap)
        if ch[node]:continue #이미 죽은 경우 -> continue
        m-=1
        ch[node]=1
        for next_node,minus in graph[node]:
            c[next_node]-=minus #하향
            heapq.heappush(heap,(c[next_node],next_node))
        answer=max(answer,poped)
    print(answer)
        
        
        