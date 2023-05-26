from collections import deque
def solution(n, computers):
    answer = 0
    que=deque()
    ch=[0]*n
    for node in range(n):
        if not ch[node]:
            answer+=1
            que.append(node)
            ch[node]=1
            while que:
                now_node=que.popleft()
                for next_node in range(n):
                    if not computers[now_node][next_node]:continue
                    if ch[next_node]:continue
                    ch[next_node]=1
                    que.append(next_node)
    
    return answer