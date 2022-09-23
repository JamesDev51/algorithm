import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def solve():
    ch=[-1]*(n+1)
    ch[n1]=0
    que=deque()
    que.append(n1)
    while que:
        node=que.popleft()
        for next_node in graph[node]:
            if ch[next_node]==-1:
                ch[next_node]=ch[node]+1
                que.append(next_node)
    return ch[n2]
    


if __name__=="__main__":
    n=int(input())
    n1,n2=map(int,input().split())
    m=int(input())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(solve())