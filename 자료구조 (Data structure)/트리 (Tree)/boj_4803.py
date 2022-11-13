import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    ch=[0]*(n+1)
    cnt=0
    que=deque()
    for node in range(1,n+1):
        if not ch[node]:
            flag=True
            ch[node]=1
            que.append((node,0))
            while que:
                parents,before = que.pop()
                for child in graph[parents]:
                    if child==before: continue
                    if ch[child]: flag=False
                    else:
                        ch[child]=1
                        que.append((child,parents))
            if flag:cnt+=1
        
    if cnt==0:
        return "No trees."
    elif cnt==1:
        return "There is one tree."
    else:
        return f"A forest of {cnt} trees."

if __name__=="__main__":
    T=1
    while True:
        n,m=map(int,input().split())
        if not n and not m:break
        graph=[[] for _ in range(n+1)]
        for _ in range(m):
            n1,n2=map(int,input().split())
            graph[n1].append(n2)
            graph[n2].append(n1)
        print(f"Case {T}: "+solve())
        T+=1 