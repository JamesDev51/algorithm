import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    que=deque(); que.append((0,0))
    ch=[[(-1)]*m for _ in range(n)]; ch[0][0]=1
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and ch[ny][nx]==-1 and mat[ny][nx]:
                ch[ny][nx]=ch[y][x]+1
                que.append((ny,nx))
    return ch[n-1][m-1]
    
if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().strip())) for _ in range(n)]
    print(bfs())