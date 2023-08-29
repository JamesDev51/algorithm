from collections import deque

def make_graph(n,edge):
    graph=[[] for _ in range(n+1)]
    for v1,v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def solution(n, edge):
    answer = 0
    graph=make_graph(n,edge)
    ch=[0]*(n+1);ch[1]=1
    que=deque();que.append((1,0))
    
    max_dist=float('-inf')
    while que:
        node,dist=que.popleft()
        if max_dist<dist:
            max_dist=dist;answer=1
        elif max_dist==dist:
            answer+=1
        for next_node in graph[node]:
            if not ch[next_node]:
                ch[next_node]=1
                que.append((next_node,dist+1))
    return answer