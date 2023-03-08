import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    k=int(input())
    w,h=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(h)]
    que=deque();que.append((0,0,k))
    ch=[[[-1]*(k+1) for _ in range(w)] for _ in range(h)];ch[0][0][k]=0
    
    while que:
        y,x,chance=que.popleft()
        if chance>0:
            for dy,dx in zip([-2,-1,1,2,2,1,-1,-2],[1,2,2,1,-1,-2,-2,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<h and 0<=nx<w and not mat[ny][nx] and ch[ny][nx][chance-1]==-1:
                    ch[ny][nx][chance-1]=ch[y][x][chance]+1
                    que.append((ny,nx,chance-1))
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w  and not mat[ny][nx] and ch[ny][nx][chance]==-1:
                ch[ny][nx][chance]=ch[y][x][chance]+1
                que.append((ny,nx,chance))
    res=float('inf')
    for val in ch[h-1][w-1]:
        if val!=-1:res=min(res,val)
    print(res if res!=float('inf') else -1)