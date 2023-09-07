from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    for n1,n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
    que=deque();que.append(destination)
    ch=[-1]*(n+1);ch[destination]=0
    
    while que:
        node=que.popleft()
        for next_node in graph[node]:
            if ch[next_node]==-1:
                ch[next_node]=ch[node]+1
                que.append(next_node)
    for source in sources:
        answer.append(ch[source])

    return answer