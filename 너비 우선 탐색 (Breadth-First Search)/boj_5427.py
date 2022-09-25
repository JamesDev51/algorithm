import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

def solve():
    que=deque(); tmp_que=deque()
    fire_que=deque(); tmp_fire_que=deque()
    ch=[[-1]*w for _ in range(h)]
    fire_ch=[[0]*w for _ in range(h)]
    
    for y in range(h):
        for x in range(w):
            if mat[y][x]=='@': que.append((y,x)); ch[y][x]=0
            if mat[y][x]=='*': fire_que.append((y,x)); fire_ch[y][x]=1
    while que or fire_que:
        while fire_que:
            y,x=fire_que.popleft() 
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<h and 0<=nx<w and mat[ny][nx]!='#' and not fire_ch[ny][nx]:
                    fire_ch[ny][nx]=1
                    mat[ny][nx]='*'
                    tmp_fire_que.append((ny,nx))
        fire_que=deepcopy(tmp_fire_que)
        tmp_fire_que.clear()
        
        while que:
            y,x=que.popleft()
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<h and 0<=nx<w :
                    if mat[ny][nx] not in "*#" and ch[ny][nx]==-1:
                        ch[ny][nx]=ch[y][x]+1
                        tmp_que.append((ny,nx))
                else:
                    return ch[y][x]+1
        que=deepcopy(tmp_que)
        tmp_que.clear()
    return "IMPOSSIBLE"
    
if __name__=="__main__":
    for _ in range(int(input())):
        w,h=map(int,input().split())
        mat=[list(input().strip()) for _ in range(h)]
        print(solve())