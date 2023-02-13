import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        k,m,p=map(int,input().split())
        tails=[0]*(m+1)
        graph=[[] for _ in range(m+1)]
        for _ in range(p):
            a,b=map(int,input().split())
            graph[a].append(b)
            tails[b]+=1
        que=deque()
        strahler_tails=[[0,0] for _ in range(m+1)]
        for node in range(1,m+1):
            if not tails[node]:
                que.append((node,1))
                strahler_tails[node]=[1,1]

        while que:
            node,strahler = que.popleft()
            
            for next_node in graph[node]:
                tails[next_node]-=1
                if strahler>strahler_tails[next_node][0]:strahler_tails[next_node]=[strahler,1]
                elif strahler==strahler_tails[next_node][0]:strahler_tails[next_node][1]+=1
                
                if not tails[next_node]:
                    if strahler_tails[next_node][1]>=2:que.append((next_node,strahler_tails[next_node][0]+1))
                    else:que.append((next_node,strahler_tails[next_node][0]))
        
        res=float('-inf')
        for node in range(1,m+1):
            st,cnt=strahler_tails[node]
            if cnt>=2:res=max(res,st+1)
            else:res=max(res,st)
        print(k,res)
                
                
                
                
                                