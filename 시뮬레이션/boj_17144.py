import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def spread():
    for y in range(r):
        for x in range(c):
            if mat[y][x]<5:continue
            cnt=0
            amount=mat[y][x]//5
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<r and 0<=nx<c and mat[ny][nx]!=-1:
                    cnt+=1
                    que.append((ny,nx,amount))
            mat[y][x]-=(cnt*amount)
    while que:
        y,x,amount=que.popleft()
        mat[y][x]+=amount

def fresh():
    d=1
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    y,x=fresher[0][0],fresher[0][1]+1
    while mat[y][x]!=-1:
        ny,nx=y+dy[d],x+dx[d]
        if not 0<=ny<r or not 0<=nx<c:
            d=(d+3)%4
            ny,nx=y+dy[d],x+dx[d]
        if mat[y][x]>0:
            if mat[ny][nx]!=-1:que.append((ny,nx,mat[y][x]))
            mat[y][x]=0
        y,x=ny,nx
    d=1
    y,x=fresher[1][0],fresher[1][1]+1
    while mat[y][x]!=-1:
        ny,nx=y+dy[d],x+dx[d]
        if not 0<=ny<r or not 0<=nx<c:
            d=(d+1)%4
            ny,nx=y+dy[d],x+dx[d]
        if mat[y][x]>0:
            if mat[ny][nx]!=-1:que.append((ny,nx,mat[y][x]))
            mat[y][x]=0
        y,x=ny,nx

    while que:
        y,x,amount=que.popleft()
        mat[y][x]+=amount
                    
if __name__=="__main__":
    r,c,t=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(r)]
    fresher=[] #0이 위, 1이 아래
    for y in range(r):
        for x in range(c):
            if mat[y][x]==-1: fresher.append((y,x))
    que=deque()
    for _ in range(t):
        spread()
        fresh()
    res=0
    for y in range(r):
        for x in range(c):
            if mat[y][x]>0:res+=mat[y][x]
    print(res)
    
    