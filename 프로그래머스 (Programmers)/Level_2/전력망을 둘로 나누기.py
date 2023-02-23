
answer=0
graph=[[] for _ in range(101)]
ch=[0]*101
def dfs(node,n):
    global answer
    right=1
    for next_vertex in graph[node]:
        if not ch[next_vertex]:
            ch[next_vertex]=1
            right+=dfs(next_vertex,n)
    answer=min(answer,abs(right-(n-right)))
    return right
def solution(n, wires):
    global answer
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    ch[1]=1
    answer=n
    dfs(1,n)
        
    return answer