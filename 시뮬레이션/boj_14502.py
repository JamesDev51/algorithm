import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy

def check():
    global res
    virus_que=deque(virus)
    cp_ch=deepcopy(ch)
    while virus_que:
        y,x=virus_que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and mat[ny][nx]==0 and not cp_ch[ny][nx]:
                cp_ch[ny][nx]=1
                virus_que.append((ny,nx))
    safe=0
    for y in range(n):
        for x in range(m):
            if not mat[y][x] and not cp_ch[y][x]:
                safe+=1
    res=max(res,safe)
    

def go(wall,idx):
    if wall==3:
        check()
        return
    if idx==len(empty):return
    for i in range(idx,len(empty)):
        y,x=empty[i]
        mat[y][x]=1
        go(wall+1,i+1)
        mat[y][x]=0
        
        

if __name__=="__main__":
    res=float('-inf')
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    virus=list()
    empty=list()
    for y in range(n):
        for x in range(m):
            if mat[y][x]==2:virus.append((y,x));ch[y][x]=1
            if mat[y][x]==0:empty.append((y,x))
            
    go(0,0)
    print(res)
    