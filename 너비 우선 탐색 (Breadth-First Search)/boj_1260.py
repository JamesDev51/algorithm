import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def dfs(start):
    stack=[]; stack.append(start)
    ch=[0]*(n+1)
    while stack:
        node=stack.pop()
        if not ch[node]:
            ch[node]=1 
            print(node,end=" ")
            for next_node in sorted(graph[node],reverse=True):
                if not ch[next_node]:
                    stack.append(next_node)
    print()
def bfs(start):
    que=deque(); que.append(start)
    ch=[0]*(n+1); ch[start]=1
    while que:
        node=que.popleft()
        print(node,end=" ")
        for next_node in sorted(graph[node]):
            if not ch[next_node]:
                ch[next_node]=1
                que.append(next_node)
    

if __name__=="__main__":
    n,m,v=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        n1,n2=map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    dfs(v)
    bfs(v)
        