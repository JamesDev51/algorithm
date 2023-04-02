import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def go():
    que=deque()
    time=0;size=2;cnt=0
    for y in range(n):
        for x in range(n):
            if mat[y][x]==9:sy,sx=y,x;mat[y][x]=0
    while True:
        que.append((sy,sx,0))
        ch=[[0]*n for _ in range(n)];ch[sy][sx]=1
        flag=False
        fishes=[]
        while que:
            y,x,can=que.popleft()
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<n and 0<=nx<n and not ch[ny][nx] and mat[ny][nx]<=size:
                    ch[ny][nx]=1
                    que.append((ny,nx,can+1))
                    if 0<mat[ny][nx]<size:
                        fishes.append((ny,nx,can+1))
        if fishes:
            fishes.sort(key=lambda x:(x[2],x[0],x[1]))
            nsy,nsx,can=fishes[0]
            time+=(can)
            sy,sx=nsy,nsx
            mat[sy][sx]=0
            cnt+=1
            if cnt==size:size+=1;cnt=0
            flag=True
        if not flag:break
    return time

if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(go())