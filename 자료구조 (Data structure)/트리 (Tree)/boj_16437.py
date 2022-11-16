import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(int(1e9))
from collections import deque
input=sys.stdin.readline

def dfs(node):
    ret=sheep[node]
    for next_node in graph[node]:
        if not ch[next_node]:
            ch[next_node]=1
            ret+=dfs(next_node)
    return max(0,ret-wolves[node])
    
    

if __name__=="__main__":
    n=int(input())
    graph=[[] for _ in range(n+1)]
    wolves=[0]*(n+1)
    sheep=[0]*(n+1)
    for node in range(2,n+1):
        t,a,p=input().split();
        a=int(a); p=int(p)
        graph[p].append(node)
        if t=='S': sheep[node]=a
        else: wolves[node]=a
    ch=[0]*(n+1); ch[1]=1
    print(dfs(1))
        