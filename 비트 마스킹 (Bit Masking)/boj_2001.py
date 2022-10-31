import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    ch=[[0]*(1<<k+2) for _ in range(n+1)]
    ch[1][0]=1
    que=deque()
    que.append((1,0,0))
    
    res=[0]*(n+1)
    while que:
        now, visited,cnt=que.popleft()
        res[now]=max(res[now], cnt)

        for next, limit in graph[now]:
            if cnt<=limit and not ch[next][visited]:
                ch[next][visited]=1
                que.append((next,visited,cnt))
            if jew & 1<<next and cnt<=limit and  not ch[next][visited | 1<<idx_dict[next]]:
                ch[next][visited | 1 <<idx_dict[next]] = 1 
                que.append((next,visited | 1<<idx_dict[next],cnt+1))
    return res[1]

if __name__=="__main__":
    n,m,k=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    jew=0
    idx_dict=dict()
    for i in range(1,k+1): 
        node=int(input()); 
        jew |= 1<<node
        idx_dict[node]=i
    for _ in range(m):
        a,b,c=map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    print( solve())