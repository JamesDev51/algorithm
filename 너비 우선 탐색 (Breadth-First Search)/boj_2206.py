import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    ch=[[[-1]*2 for _ in range(m)] for _ in range(n)]
    ch[0][0][0]=1
    que=deque()
    que.append((0,0,0))
    
    while que:
        y,x,cap = que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m:
                if mat[ny][nx] and not cap and ch[ny][nx][1]==-1: que.append((ny,nx,1)); ch[ny][nx][1]=ch[y][x][0]+1
                if not mat[ny][nx] and ch[ny][nx][cap]==-1: que.append((ny,nx,cap)); ch[ny][nx][cap]=ch[y][x][cap]+1 
    return max(ch[n-1][m-1]) if min(ch[n-1][m-1]) == -1 else min(ch[n-1][m-1])

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().strip())) for _ in range(n)]
    print(solve())