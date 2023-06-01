from collections import deque
graph=dict()
ch=dict()
def make_graph(words):
    for word1 in words:
        graph[word1]=[]
        ch[word1]=0
        for word2 in words:
            if word1==word2:continue
            diff_cnt=0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:diff_cnt+=1
            if diff_cnt==1:
                graph[word1].append(word2)
def bfs(start,end):
    que=deque()
    ch[start]=1
    que.append((start,0))
    while que:
        node,cnt=que.popleft()
        if node==end:return cnt
        for next_node in graph[node]:
            if not ch[next_node]:
                ch[next_node]=1
                que.append((next_node,cnt+1))
    return 0
    
            
def solution(begin, target, words):
    words.append(begin)
    make_graph(words)
    answer=bfs(begin,target)
    return answer