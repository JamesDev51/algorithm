import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque


if __name__=="__main__":
    n,m=map(int,input().split())
    tmp=map(int,input().split())
    truth_people_cnt=next(tmp)
    truth_people=list(tmp)
    truth_ch=[0]*(n+1)
    for tp in truth_people:
        truth_ch[tp]=1
    graph=[set() for _ in range(n+1)]
    parties=[]
    for _ in range(m):
        tmp=map(int,input().split())
        party_people_cnt=next(tmp)
        party_people=list(tmp)
        parties.append(party_people)
        for p1 in party_people:
            for p2 in party_people:
                if p1==p2:continue
                graph[p1].add(p2)
                graph[p2].add(p1)

    ch=[0]*(n+1)
    que=deque()
    
    for i in range(1,n+1):
        if truth_ch[i] and not ch[i]:
            ch[i]=1
            que.append(i)
            while que:
                p=que.popleft()
                for np in graph[p]:
                    if not truth_ch[np] and not ch[np]:
                        ch[np]=1
                        truth_ch[np]=1
                        que.append(np)
    answer=0
    for party in parties:
        flag=True
        for p in party:
            if truth_ch[p]:
                flag=False
                break
        if flag:
            answer+=1
    print(answer)
    