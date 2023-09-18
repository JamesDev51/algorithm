import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    
    answer=[[-1]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if mat[y][x]==2:sy,sx=y,x
            if mat[y][x]==0:answer[y][x]=0
            
    answer[sy][sx]=0
    que=deque()
    que.append((sy,sx))
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and answer[ny][nx]==-1 and mat[ny][nx]!=0:
                answer[ny][nx]=answer[y][x]+1
                que.append((ny,nx))
    for q in answer:
        print(*q)
    
            