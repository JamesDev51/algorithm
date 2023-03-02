import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    longest=-1;ans=-1
    for yy in range(n):
        for xx in range(m):
            if mat[yy][xx]==0:continue
            que=deque();que.append((yy,xx))
            ch=[[0]*m for _ in range(n)];ch[yy][xx]=1
            while que:
                y,x=que.popleft()
                if longest<=ch[y][x]:
                    if longest<ch[y][x]:ans=mat[yy][xx]+mat[y][x]
                    else:ans=max(ans,mat[yy][xx]+mat[y][x])
                    longest=max(longest,ch[y][x])
                for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<m and mat[ny][nx]!=0 and ch[ny][nx]==0:
                        que.append((ny,nx))
                        ch[ny][nx]=ch[y][x]+1
    print(ans)
            
            