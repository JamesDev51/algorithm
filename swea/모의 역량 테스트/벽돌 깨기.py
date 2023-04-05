import sys
sys.stdin=open("input.text","rt")

from copy import deepcopy
from collections import deque

que=deque()
def break_down():
    global res
    cp_mat=deepcopy(mat)
    for c in used:
        r=0
        while r<h and not cp_mat[r][c]:r+=1
        if r==h:continue
        que.append((r,c,cp_mat[r][c]))
        cp_mat[r][c]=0
        while que:
            y,x,num=que.popleft()        
            for power in range(1,num):
                for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                    ny,nx=y+dy*power,x+dx*power
                    if 0<=ny<h and 0<=nx<w:
                        if cp_mat[ny][nx]>1:que.append((ny,nx,cp_mat[ny][nx]))
                        cp_mat[ny][nx]=0
        for x in range(w):
            real_y=h-1
            for y in range(h-1,-1,-1):
                if cp_mat[y][x]>0:
                    cp_mat[real_y][x],cp_mat[y][x]=cp_mat[y][x],cp_mat[real_y][x]
                    real_y-=1
    cnt=0
    for y in range(h):
        for x in range(w):
            if cp_mat[y][x]>0:cnt+=1
    res=min(res,cnt)

def go(cnt):
    if res==0:return
    if cnt==n:break_down();return
    for col in range(w): 
        used.append(col)
        go(cnt+1)
        used.pop()
    
for t in range(1,int(input())+1):
    n,w,h=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(h)]
    used=[]
    res=float('inf')
    go(0)
    print(f"#{t} {res}")