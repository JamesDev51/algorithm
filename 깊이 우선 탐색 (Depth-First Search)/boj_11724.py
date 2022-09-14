import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    for next_node in graph[node]:
        if not ch[next_node]:
            ch[next_node]=1
            dfs(next_node)
def solve():
    res=0
    for node in range(1,n+1):
        if not ch[node]:
            res+=1
            ch[node]=1
            dfs(node)
    return res

if __name__=="__main__":
    n,m=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        graph[u].append(v); graph[v].append(u)
    ch=[0]*(n+1)
    print(solve())