import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def bfs(start_node):
    que=deque();que.append((start_node,0))
    ch=[0]*(n+1); ch[start_node]=1
    far=[-1,float('-inf')]
    while que:
        node,cost=que.popleft()
        if cost>far[1]:far=[node,cost]
        for next_node,next_cost in tree[node]:
            if not ch[next_node]:
                ch[next_node]=1                
                new_cost=cost+next_cost
                que.append((next_node,new_cost))
    return far

if __name__=="__main__":
    n=int(input())
    tree=[[] for _ in range(n+1)] 
    for _ in range(n-1):
        p,c,cost=map(int,input().split())
        tree[p].append((c,cost))
        tree[c].append((p,cost))
    far_node,_=bfs(1)
    far_node2,far_cost2=bfs(far_node)
    print(far_cost2)