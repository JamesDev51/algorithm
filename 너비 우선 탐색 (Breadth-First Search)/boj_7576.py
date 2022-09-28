import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    que=deque()
    ch=[[-1]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if mat[y][x]==1:
                ch[y][x]=0
                que.append((y,x))
    
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and mat[ny][nx]==0 and ch[ny][nx]==-1:
                ch[ny][nx]=ch[y][x]+1
                que.append((ny,nx))
                
    for y in range(n):
        for x in range(m):
            if mat[y][x]==0 and ch[y][x]==-1: return -1
    return max(ch[i][j] for j in range(m) for i in range(n))

if __name__=="__main__":
    m,n=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(bfs())