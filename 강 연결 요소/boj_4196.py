import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000000)

def dfs(node):
    if not ch[node]:
        ch[node]=1
        for next_node in graph[node]:
            if not ch[next_node]:
                dfs(next_node)
        stack.append(node)
    
def rev_dfs(node):
    if not ch[node]:
        ch[node]=1
        scc[node]=scc_cnt
        for next_node in rev_graph[node]:
            if not ch[next_node]:
                rev_dfs(next_node)

def scc_dfs(node):
    if not ch[node]:
        ch[node]=1
        for next_node in graph[node]:
            if scc[node]!=scc[next_node]:scc_indegree[scc[next_node]]+=1
            if not ch[next_node]:
                scc_dfs(next_node)

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().split())
        stack=[]
        graph=[[] for _ in range(n+1)]
        rev_graph=[[] for _ in range(n+1)]
        for _ in range(m):
            n1,n2=map(int,input().split())
            graph[n1].append(n2)
            rev_graph[n2].append(n1)
        ch=[0]*(n+1)
        for node in range(1,n+1):
            dfs(node)
            
        ch=[0]*(n+1)
        scc=[0]*(n+1);scc_cnt=1
        while stack:
            poped=stack.pop()
            if not ch[poped]:
                rev_dfs(poped) 
                scc_cnt+=1
                
        scc_indegree=[0]*scc_cnt
        ch=[0]*(n+1)
        for node in range(1,n+1):
            if not ch[node]:
                scc_dfs(node)
        print(scc_indegree[1:].count(0))
            