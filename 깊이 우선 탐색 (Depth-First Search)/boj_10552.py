import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(now,cnt):
    if not graph[now]: return cnt
    visited[now]=1
    next=graph[now]
    if visited[next]: return -1
    ret=dfs(next,cnt+1)
    return ret
    

if __name__=="__main__":
    n,m,p=list(map(int,input().split()))
    graph=[0]*(m+1)
    for _ in range(n):
        n1,n2=map(int,input().split())
        if not graph[n2]: graph[n2]=n1
    visited=[0]*(m+1)
    print(dfs(p,0))