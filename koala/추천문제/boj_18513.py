import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from collections import deque

if __name__=="__main__":
    n,k=map(int,input().split())
    samtus=list(map(int,input().split()))
    que=deque()
    visited=set()
    for samtu in samtus:
        visited.add(samtu)
        que.append((samtu,1))
    res=0
    
    while que:
        pos,dist = que.popleft()
        flag=False
        if (pos-dist) not in visited:
            visited.add(pos-dist)
            res+=dist
            flag=True
        if len(visited)==n+k:break
        
        if (pos+dist) not in visited:
            visited.add(pos+dist)
            res+=dist
            flag=True
        if len(visited)==n+k:break
        if flag:que.append((pos,dist+1))
    print(res)
    
        
        
            
            
    
    
            
            
        