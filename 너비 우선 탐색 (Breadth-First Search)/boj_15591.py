import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    n,question=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(n-1):
        p,q,r=map(int,input().split())
        graph[p].append((q,r))
        graph[q].append((p,r))
    usado_table=[[0]*(n+1) for _ in range(n+1)]
    que=deque()
    for s_node in range(1,n+1):
        ch=[0]*(n+1); ch[s_node]=1
        que.clear(); que.append((s_node,float('inf')))
        while que:
            node,min_usado=que.popleft()
            for next_node,usado in graph[node]:
                if ch[next_node]==1:continue
                usado_table[s_node][next_node]=min(min_usado,usado)
                ch[next_node]=1
                que.append((next_node,min(min_usado,usado)))
    
    for _ in range(question):
        k,v=map(int,input().split())
        cnt=0
        for i in range(1,n+1):
            if usado_table[v][i]>=k:cnt+=1
        print(cnt)