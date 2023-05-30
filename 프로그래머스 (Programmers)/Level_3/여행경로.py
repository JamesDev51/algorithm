from collections import deque

answer = []
graph=dict()
ch=dict()
total_cnt=-1
def dfs(node,cnt):
    if cnt==total_cnt:return True
    ret=False
    for next_node in sorted(graph[node]):
        if ch[(node,next_node)]>0:
            ch[(node,next_node)]-=1
            answer.append(next_node)
            ret=dfs(next_node,cnt+1)
            if ret:break
            ch[(node,next_node)]+=1
            answer.pop()
    return ret
            


def solution(tickets):
    global total_cnt
    total_cnt=len(tickets)
    for a,b in tickets:
        if a not in graph:graph[a]=[]
        if b not in graph:graph[b]=[]
        graph[a].append(b)
        if (a,b) not in ch:ch[(a,b)]=0
        ch[(a,b)]+=1
    answer.append("ICN")
    dfs("ICN",0)
    return answer