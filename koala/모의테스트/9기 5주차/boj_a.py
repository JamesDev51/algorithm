import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


def bfs():
    que=deque()
    que.append(1)
    ch=[0]*(n+1);ch[1]=1
    while que:
        node=que.popleft()    
        for next_node in graph[node]:
            if not ch[next_node]:
                ch[next_node]=1
                que.append(next_node)
    return sum(ch)-1

if __name__=="__main__":
    n=int(input())
    graph=[[] for _ in range(n+1)]
    for _ in range(int(input())):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs())