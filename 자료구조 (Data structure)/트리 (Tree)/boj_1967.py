import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    if n==1: print(0); exit(0)
    tree=[[] for _ in range(n+1)]
    tail=[0]*(n+1)
    child_sum=[[] for _ in range(n+1)]
    child_big=[0]*(n+1)
    
    for _ in range(n-1):
        parents,child, length=map(int,input().split())
        tree[child]=[parents,length]
        tail[parents]+=1
    
    que=deque()
    for node in range(1,n+1):
        if not tail[node]: que.append((node,0))

    while que:
        child,pre_length=que.popleft()
        if tree[child]:
            parents,length=tree[child]
            tail[parents]-=1
            heapq.heappush(child_sum[parents],-(pre_length+length))
            child_big[parents]=max(child_big[parents],pre_length+length)
            if not tail[parents]: que.append((parents,child_big[parents]))
    
    res=float('-inf')
    for parents in range(1,n+1):
        if len(child_sum[parents])>=2:
            val1=heapq.heappop(child_sum[parents])
            val2=heapq.heappop(child_sum[parents])
            res=max(res,-(val1+val2))
        elif len(child_sum[parents])==1:        
            val=heapq.heappop(child_sum[parents])
            res=max(res,-(val))
    
    print(res)
        