from collections import deque
def solution(n, results):
    answer = 0
    graph=[[] for _ in range(n+1)]
    match=[[0]*(n+1) for _ in range(n+1)]

    for win_node,lose_node in results:
        graph[lose_node].append(win_node)
        
    que=deque()
    for win_node,lose_node in results:
        ch=[0]*(n+1);ch[lose_node]=1
        que.append(win_node)
        while que:
            node=que.popleft()
            match[lose_node][node]=1
            match[node][lose_node]=1
            for next_win_node in graph[node]:
                if not ch[next_win_node]:
                    ch[next_win_node]=1
                    que.append(next_win_node)
    
    for q in match:
        if sum(q)==n-1:answer+=1
            

    return answer